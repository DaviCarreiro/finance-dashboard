from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from finance_dashboard.db.base import Base
from finance_dashboard.models.categoria import Categoria
from finance_dashboard.models.usuario import Usuario

class Transacao(Base):
    __tablename__ = "transacoes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str]
    valor: Mapped[float]
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categoria.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    categoria: Mapped["Categoria"] = relationship()
    usuario: Mapped["Usuario"] = relationship()