from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///instrumentos.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()