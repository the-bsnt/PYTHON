import os
from dotenv import load_dotenv


load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = os.getenv("DB_ENGINE")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

# dialect://user:password@host:port/dbname
DATABASE_URL = f"{engine}://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
