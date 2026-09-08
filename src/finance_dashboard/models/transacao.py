from sqlalchemy.orm import Mapped, mapped_column
from finance_dashboard.db.base import Base

class Transacao(Base):
    __tablename__ = "transacoes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str]
    valor: Mapped[float]