from sqlalchemy import Column, String, Float, Date
from model.base import Base

class Instrumento(Base):
    __tablename__ = "instrumentos"

    tag = Column(String, primary_key=True)
    lrv = Column(Float, nullable=False)
    urv = Column(Float, nullable=False)
    span = Column(Float, nullable=False)
    data_loop = Column(Date, nullable=False)

    def __init__(self, tag, lrv, urv, data_loop):
        self.tag = tag
        self.lrv = lrv
        self.urv = urv
        self.span = urv - lrv
        self.data_loop = data_loop