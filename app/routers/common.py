from fastapi import HTTPException, UploadFile

from sqlalchemy import func

from app.schemas import Prediction, Stats
from app.ml import infer
from app.database import SessionLocal
from app.models import Votes, Logs

from fastapi import APIRouter, Request, UploadFile, HTTPException
from fastapi_cache.decorator import cache

router = APIRouter()

# проголосовать
@router.post("/vote")
def common_vote(vote: int, request: Request) -> str:

    # у нас и в базе есть констрейнт, но лучше заранее проверить тоже
    if not (0 < vote < 6):
        raise HTTPException(status_code=406, detail="Votes should be between 1 and 6")

    client_ip = request.client.host
    
    session = SessionLocal()
    session.add(Votes(ip = client_ip , rating = vote))
    session.commit()

    return f"Your vote {vote} saved"


# сделать предсказание
@router.post("/predict")
def common_predict(file: UploadFile, request: Request) -> Prediction:

    text = ''.join([line.decode('utf-8') for line in  file.file.readlines()])
    label, name, value = infer(text)

    client_ip = request.client.host

    session = SessionLocal()
    session.add(Logs(ip = client_ip, request = text))
    session.commit()

    return Prediction(label=label, name=name, value=value)


# просмотреть статистику
@router.get("/stat")
@cache(expire=30) 
def common_stat() -> Stats:

    session = SessionLocal()
    votes, rating = session.query(func.count(Votes.rating), func.avg(Votes.rating)).one()

    return Stats(total_votes = votes, avg_rating = rating)

