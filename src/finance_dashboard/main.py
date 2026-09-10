from fastapi import FastAPI

from finance_dashboard.api.routes_transacoes import router as router_transacoes
from finance_dashboard.api.routes_categorias import router as router_categorias
from finance_dashboard.api.routes_usuarios import router as router_usuarios

app = FastAPI()

app.include_router(router_transacoes)
app.include_router(router_categorias)
app.include_router(router_usuarios)