 #sabe de banco de dados — não sabe nada de HTTP, status code, etc
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
from schemas import Produto


def buscar_produto_ou_404(produto_id: int, db: Session):
    produto_db = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto_db


def listar_produtos(db: Session):
    return db.query(models.Produto).all()


def criar_produto(produto: Produto, db: Session):
    novo_produto = models.Produto(nome=produto.nome, quantidade=produto.quantidade)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto


def atualizar_produto(produto_id: int, produto: Produto, db: Session):
    produto_db = buscar_produto_ou_404(produto_id, db)
    produto_db.nome = produto.nome
    produto_db.quantidade = produto.quantidade
    db.commit()
    db.refresh(produto_db)
    return produto_db


def deletar_produto(produto_id: int, db: Session):
    produto_db = buscar_produto_ou_404(produto_id, db)
    db.delete(produto_db)
    db.commit()
    return {"mensagem": f"Produto {produto_id} removido"}