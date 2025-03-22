from sqlalchemy import Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)

class Instrumento(Base):
    __tablename__ = 'instrumentos'
    tag = Column(String, primary_key=True)
    urv = Column(Float, nullable=False)
    lrv = Column(Float, nullable=False)
    span = Column(Float, nullable=False)
    data_loop = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Instrumento(tag={self.tag}, URV={self.urv}, LRV={self.lrv}, SPAN={self.span}, Data={self.data_loop})>"
Base.metadata.create_all(engine)
