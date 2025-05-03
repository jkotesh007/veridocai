from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./app.db" #SQLite database file
#Setup database connection and setup
engine=create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#Base class for models
Base=declarative_base()

#Initialize DB
def init_db():
    Base.metadata.create_all(bind=engine)
    