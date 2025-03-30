from pydantic import BaseModel, Field
from datetime import date
from typing import List

class InstrumentoIn(BaseModel):
    tag: str = Field(..., example="PIT-3001")
    lrv: float = Field(..., example=0.0)
    urv: float = Field(..., example=150.0)
    data_loop: date = Field(..., example="2025-03-22")

class InstrumentoOut(InstrumentoIn):
    span: float = Field(..., example=150.0)

class InstrumentoBusca(BaseModel):
    tag: str = Field(..., example="PIT-3001")

class InstrumentoDel(BaseModel):
    message: str
    tag: str

class InstrumentoListOut(BaseModel):
    instrumentos: List[InstrumentoOut]