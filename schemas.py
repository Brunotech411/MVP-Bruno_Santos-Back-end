from pydantic import BaseModel
from typing import List
from datetime import date

class InstrumentoSchema(BaseModel):
    tag: str
    lrv: float
    urv: float
    data_loop: date

    class Config:
        json_schema_extra = {
            "example": {
                "tag": "TIT-2042",
                "lrv": 0.0,
                "urv": 150.0,
                "data_loop": "2025-03-22"
            }
        }

class InstrumentoBuscaSchema(BaseModel):
    tag: str

class InstrumentoViewSchema(BaseModel):
    tag: str
    lrv: float
    urv: float
    span: float
    data_loop: date

class ListagemInstrumentosSchema(BaseModel):
    instrumentos: List[InstrumentoViewSchema]

class InstrumentoDelSchema(BaseModel):
    mensagem: str
    tag: str

class ErrorSchema(BaseModel):
    message: str