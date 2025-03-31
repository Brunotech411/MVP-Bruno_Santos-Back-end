from pydantic import BaseModel, Field
from typing import List

class InstrumentoIn(BaseModel):
    """Define os dados necessários para cadastrar um instrumento"""
    tag: str = Field(..., example="PIT-3001")
    lrv: float = Field(..., example=0.0)
    urv: float = Field(..., example=100.0)
    data_loop: str = Field(..., example="2025-03-30")

class InstrumentoOut(InstrumentoIn):
    """Define o formato de saída de um instrumento, incluindo o SPAN calculado"""
    span: float = Field(..., example=100.0)

class InstrumentoBusca(BaseModel):
    """Define o formato da requisição de busca por TAG"""
    tag: str = Field(..., example="PIT-3001")

class InstrumentoDel(BaseModel):
    """Define a resposta da remoção de um instrumento"""
    message: str
    tag: str

class InstrumentoListOut(BaseModel):
    """Define o formato de resposta ao listar vários instrumentos"""
    instrumentos: List[InstrumentoOut]
