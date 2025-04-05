from sqlalchemy import Column, String, Float
from database.base import Base

# Modelo ORM da tabela "instrumentos"
class Instrumento(Base):
    __tablename__ = 'instrumentos'

# Define colunas da tabela com tipos e restrições
    tag = Column(String, primary_key=True)
    lrv = Column(Float, nullable=False)
    urv = Column(Float, nullable=False)
    span = Column(Float,nullable=False)
    data_loop = Column(String, nullable=False)