from pydantic import BaseModel, Field
from typing import List
from datetime import date

class InstrumentoSchema(BaseModel):
    tag: str = Field(..., example="TIT-2042")
    urv: float = Field(..., example=150.0)
    lrv: float = Field(..., example=0.0)
    span: float = Field(..., example=150.0)
    data_loop: date = Field(..., example="2025-03-22")

class InstrumentoBuscaSchema(BaseModel):
    tag: str = Field(..., example="TIT-2042")

class InstrumentoViewSchema(BaseModel):
    tag: str
    urv: float
    lrv: float
    span: float
    data_loop: date

class ListagemInstrumentosSchema(BaseModel):
    instrumentos: List[InstrumentoViewSchema]

class InstrumentoDelSchema(BaseModel):
    mensagem: str
    tag: str

class ErrorSchema(BaseModel):
    message: str
