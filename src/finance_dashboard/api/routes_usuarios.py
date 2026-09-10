from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from finance_dashboard.db.session import get_db
from finance_dashboard.models.usuario import Usuario
from finance_dashboard.schemas.usuario import UsuarioCreate, UsuarioRead

router = APIRouter()


@router.get("/usuarios", response_model=list[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios


@router.post("/usuarios", response_model=UsuarioRead)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = Usuario(nome=usuario.nome)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


@router.put("/usuarios/{usuario_id}", response_model=UsuarioRead)
def atualizar_usuario(usuario_id: int, dados: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.nome = dados.nome

    db.commit()
    db.refresh(usuario)
    return usuario


@router.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário deletado com sucesso"}