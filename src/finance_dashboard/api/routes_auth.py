from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from finance_dashboard.core.security import criar_token_acesso, gerar_hash_senha, verificar_senha
from finance_dashboard.db.session import get_db
from finance_dashboard.models.usuario import Usuario
from finance_dashboard.schemas.usuario import UsuarioRead, UsuarioRegistro

router = APIRouter()


@router.post("/auth/registrar", response_model=UsuarioRead)
def registrar(dados: UsuarioRegistro, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if usuario_existente is not None:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha_hash=gerar_hash_senha(dados.senha),
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


@router.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()

    if usuario is None or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    token = criar_token_acesso({"sub": usuario.email})

    return {"access_token": token, "token_type": "bearer"}