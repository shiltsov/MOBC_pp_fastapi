#
# загружаем sqlalchemy
#

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

pg_host = os.getenv('POSTGRES_HOST')
pg_user = os.getenv('POSTGRES_USER')
pg_password = os.getenv('POSTGRES_PASSWORD')
pg_db = os.getenv('POSTGRES_DB')

db_url = f"postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_db}"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
