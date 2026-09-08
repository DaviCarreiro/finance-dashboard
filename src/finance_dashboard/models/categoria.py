from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from finance_dashboard.db.base import Base

class Categoria(Base):
    __tablename__ = "categoria"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]