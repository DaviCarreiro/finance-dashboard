from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from finance_dashboard.db.session import get_db
from finance_dashboard.models.categoria import Categoria
from finance_dashboard.schemas.categoria import CategoriaCreate, CategoriaRead

router = APIRouter()


@router.get("/categorias", response_model=list[CategoriaRead])
def listar_categorias(db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return categorias


@router.post("/categorias", response_model=CategoriaRead)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    nova_categoria = Categoria(nome=categoria.nome)
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria


@router.put("/categorias/{categoria_id}", response_model=CategoriaRead)
def atualizar_categoria(categoria_id: int, dados: CategoriaCreate, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    categoria.nome = dados.nome

    db.commit()
    db.refresh(categoria)
    return categoria


@router.delete("/categorias/{categoria_id}")
def deletar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    db.delete(categoria)
    db.commit()

    return {"mensagem": "Categoria deletada com sucesso"}