from sqlalchemy import Column, Integer, Date, Text, String, CheckConstraint, func
from app.database import Base


# для голосований, храним каждое голосование
class Votes(Base):
    __tablename__ = "app_user_votes"

    id = Column(Integer, primary_key=True)
    ip = Column(String)
    rating = Column(Integer, index=True)
    vote_date = Column(Date, index=True, default=func.now())

    __table_args__ = (CheckConstraint("rating >= 1"), CheckConstraint("rating <= 5"))


# для логов - храним тексты, которые нам присылали
class Logs(Base):
    __tablename__ = "app_user_logs"

    id = Column(Integer, primary_key=True)
    ip = Column(String)
    request = Column(Text)
    request_date = Column(Date, index=True, default=func.now())
