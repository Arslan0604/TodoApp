# from sqlalchemy import create_engine 
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/TodoApplicationDatabase" # its for postgres
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:arslan060482@127.0.0.1:3306/TodoApplicationDatabase" #its for mysql

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()