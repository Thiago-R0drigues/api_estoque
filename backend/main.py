#sabe de rotas HTTP — não sabe como o banco funciona por dentro
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import Produto
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"mensagem": "API de estoque no ar"}


@app.get('/produtos')
def rota_listar_produtos(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)


@app.get('/produtos/{produto_id}')
def rota_buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    return crud.buscar_produto_ou_404(produto_id, db)


@app.post('/produtos')
def rota_criar_produto(produto: Produto, db: Session = Depends(get_db)):
    return crud.criar_produto(produto, db)


@app.put('/produtos/{produto_id}')
def rota_atualizar_produto(produto_id: int, produto: Produto, db: Session = Depends(get_db)):
    return crud.atualizar_produto(produto_id, produto, db)


@app.delete('/produtos/{produto_id}')
def rota_deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    return crud.deletar_produto(produto_id, db)