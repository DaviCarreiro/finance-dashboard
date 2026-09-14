from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from finance_dashboard.db.session import get_db
from finance_dashboard.models.usuario import Usuario

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "uma-chave-secreta-temporaria-trocar-depois"
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)


def criar_token_acesso(dados: dict) -> str:
    dados_para_codificar = dados.copy()
    expira_em = datetime.now(timezone.utc) + timedelta(minutes=EXPIRACAO_MINUTOS)
    dados_para_codificar.update({"exp": expira_em})
    token = jwt.encode(dados_para_codificar, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decodificar_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def obter_usuario_atual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
    payload = decodificar_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

    email = payload.get("sub")
    usuario = db.query(Usuario).filter(Usuario.email == email).first()

    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return usuario