from finance_dashboard.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Usuario(Base):
    __tablename__ = "usuario"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    