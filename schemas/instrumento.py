from pydantic import BaseModel, Field
from typing import List

# Entrada de dados para criação de instrumento
class InstrumentoIn(BaseModel):
    tag: str = Field(..., example="PIT-3001")
    lrv: float = Field(..., example=0.0)
    urv: float = Field(..., example=100.0)
    data_loop: str = Field(..., example="2025-03-30")

# Saída com SPAN calculado (herda da entrada)
class InstrumentoOut(InstrumentoIn):
    span: float = Field(..., example=100.0)

# Query param para busca por TAG
class InstrumentoBusca(BaseModel):
    tag: str = Field(..., example="PIT-3001")

# Retorno da remoção
class InstrumentoDel(BaseModel):
    message: str
    tag: str

# Lista de instrumentos
class InstrumentoListOut(BaseModel):
    instrumentos: List[InstrumentoOut]
