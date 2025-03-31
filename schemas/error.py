from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """Define o formato da mensagem de erro"""
    message: str