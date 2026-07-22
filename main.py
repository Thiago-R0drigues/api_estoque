from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, Base, get_db
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

class Produto(BaseModel):
    nome: str
    quantidade: int

@app.get("/")
def home():
    return {"mensagem": "API de estoque no ar"}

@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()

@app.post('/produtos')
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    novo_produto = models.Produto(nome=produto.nome, quantidade=produto.quantidade)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

