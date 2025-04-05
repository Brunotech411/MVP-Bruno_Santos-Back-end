from pydantic import BaseModel

# Schema de erro para padronizar respostas de falhas
class ErrorSchema(BaseModel):
    message: str