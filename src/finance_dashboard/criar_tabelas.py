from finance_dashboard.db.base import Base
from finance_dashboard.db.session import engine
from finance_dashboard.models.transacao import Transacao

Base.metadata.create_all(engine)

print("Tabelas criadas!")