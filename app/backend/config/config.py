from multiprocessing import pool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#Load environment variables from .env file
load_dotenv()

#Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured.")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping = True 
    )

SessionLocal  = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine 
    )

Base = declarative_base()

#DAtabase dependency for FastaPI
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()