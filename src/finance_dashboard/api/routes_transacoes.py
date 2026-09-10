from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from finance_dashboard.db.session import get_db
from finance_dashboard.models.transacao import Transacao
from finance_dashboard.schemas.transacao import TransacaoCreate, TransacaoRead
from fastapi import HTTPException

router = APIRouter()


@router.get("/transacoes", response_model=list[TransacaoRead])
def listar_transacoes(db: Session = Depends(get_db)):
    transacoes = db.query(Transacao).all()
    return transacoes


@router.post("/transacoes", response_model=TransacaoRead)
def criar_transacao(transacao: TransacaoCreate, db: Session = Depends(get_db)):
    nova_transacao = Transacao(
        descricao=transacao.descricao,
        valor=transacao.valor,
        categoria_id=transacao.categoria_id,
        usuario_id=transacao.usuario_id,
    )
    db.add(nova_transacao)
    db.commit()
    db.refresh(nova_transacao)
    return nova_transacao

@router.put("/transacoes/{transacao_id}", response_model=TransacaoRead)
def atualizar_transacao(transacao_id: int, dados: TransacaoCreate, db: Session = Depends(get_db)):
    transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    
    if transacao is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    
    transacao.descricao = dados.descricao
    transacao.valor = dados.valor
    transacao.categoria_id = dados.categoria_id
    transacao.usuario_id = dados.usuario_id
    
    db.commit()
    db.refresh(transacao)
    return transacao

@router.delete("/transacoes/{transacao_id}")
def deletar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    
    if transacao is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    db.delete(transacao)
    db.commit()
    
    return {"mensagem": "Transação deletada com sucesso"}