import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from dotenv import load_dotenv

load_dotenv()
Engine = create_engine(
    os.getenv("DATABASE_URL").format(
        encoding="utf-8",
        echo=True)
    )
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=Engine
    )
)

Base = declarative_base()


def create():
    Base.metadata.create_all(Engine)
