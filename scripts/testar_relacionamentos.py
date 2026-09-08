from finance_dashboard.db.session import SessionLocal
from finance_dashboard.models.usuario import Usuario
from finance_dashboard.models.categoria import Categoria
from finance_dashboard.models.transacao import Transacao

session = SessionLocal()

#cria um usuario
usuario = Usuario(nome="Davi")

#cria uma categoria
categoria = Categoria(nome="Alimentação")

#cria uma transação que liga os dois
transacao = Transacao(descricao="Almoço", valor=40, usuario=usuario, categoria=categoria)

#salva tudo no banco
session.add(transacao)
session.commit()

print(transacao.categoria.nome)
print(transacao.usuario.nome)