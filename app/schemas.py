from pydantic import BaseModel

# для common - предсказание
class Prediction(BaseModel):
    label: int
    name:  str
    value:  int | float

# для common - выдача статистики
class Stats(BaseModel):
    total_votes: int
    avg_rating: int | float

