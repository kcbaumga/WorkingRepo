from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Python.fastapi.config as config
##import mysqldb
#DATABASE_URL = config.DATABASE_URL

db_engine = create_engine("mariadb+pymysql://admin:kcb@localhost:3306/testerml")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


