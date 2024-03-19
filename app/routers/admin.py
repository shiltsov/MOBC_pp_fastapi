from fastapi import Depends, HTTPException, Response, APIRouter
from fastapi.security import OAuth2PasswordBearer
import psutil
import os
import pandas as pd
from dotenv import load_dotenv
from app.database import engine
from dotenv import load_dotenv


load_dotenv()
admin_token = os.getenv("ADMIN_TOKEN")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix="/admin")


# Создаем функцию зависимости для проверки токена
def verify_token(token: str = Depends(oauth2_scheme)):
    if token != admin_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token


# выгрузить лог голосований
@router.post("/votelog")
def admin_votelog(response: Response, token: str = Depends(verify_token)):

    df = pd.read_sql_table("app_user_votes", con=engine)
    csv_string = df.to_csv(index=False)

    response.headers["Content-Disposition"] = "attachment; filename=votes.csv"
    response.headers["Content-Type"] = "text/csv"
    return csv_string


# выгрузить лог запросов к модели
@router.post("/predictlog")
def admin_predictlog(response: Response, token: str = Depends(verify_token)) -> str:

    df = pd.read_sql_table("app_user_logs", con=engine)
    csv_string = df.to_csv(index=False)

    response.headers["Content-Disposition"] = "attachment; filename=logs.csv"
    response.headers["Content-Type"] = "text/csv"
    return csv_string


# посмотреть состояние системы
@router.get("/status")
def admin_status(token: str = Depends(verify_token)) -> dict:

    status = dict()
    status["cpu_percent"] = psutil.cpu_percent(interval=1)
    status["memory_usage"] = psutil.virtual_memory().percent
    status["disk_usage"] = psutil.disk_usage("/").percent
    status["network"] = psutil.net_io_counters()

    return status
