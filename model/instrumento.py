from sqlalchemy import Column, String, Float, Date
from database.base import Base

class Instrumento(Base):
    __tablename__ = 'instrumentos'

    tag = Column(String, primary_key=True)
    lrv = Column(Float, nullable=False)
    urv = Column(Float, nullable=False)
    data_loop = Column(String, nullable=False)