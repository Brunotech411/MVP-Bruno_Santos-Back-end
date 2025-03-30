from pydantic import BaseModel, Field

class InstrumentoIn(BaseModel):
    tag: str = Field(..., example="PIT-3001")
    lrv: float = Field(..., example=0.0)
    urv: float = Field(..., example=100.0)
    data_loop: str = Field(..., example="2025-03-30")

class InstrumentoOut(InstrumentoIn):
    span: float = Field(..., example=100.0)

class InstrumentoBusca(BaseModel):
    tag: str = Field(..., example="PIT-3001")

class InstrumentoDel(BaseModel):
    message: str
    tag: str

class InstrumentoListOut(BaseModel):
    instrumentos: list[InstrumentoOut]
