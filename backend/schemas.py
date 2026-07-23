#define o formato dos dados que entram/saem da API
from pydantic import BaseModel


class Produto(BaseModel):
    nome: str
    quantidade: int