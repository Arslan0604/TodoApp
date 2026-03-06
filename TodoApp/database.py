from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os   # this I have added to fix
from dotenv import load_dotenv

load_dotenv()

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/TodoApplicationDatabase" # its for postgres
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:arslan060482@127.0.0.1:3306/TodoApplicationDatabase" #its for mysql
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL") # this I have added last
# DATABASE_URL = "postgresql://todo_postgresql_y4y6_user:kju4dELbNR5BQQXVTM4oIZGpL6l6SLFK@dpg-d688mhogjchc73beu4pg-a.oregon-postgres.render.com/todo_postgresql_y4y6"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# import os

# SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

# # 🔥 если запускаем локально и переменной нет
# if not SQLALCHEMY_DATABASE_URL:
#     SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# # 🔥 фикс для Render (если начинается с postgres://)
# if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
#     SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
#         "postgres://", "postgresql://", 1
#     )

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
