from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from finance_dashboard.api.routes_transacoes import router as router_transacoes
from finance_dashboard.api.routes_categorias import router as router_categorias
from finance_dashboard.api.routes_usuarios import router as router_usuarios
from finance_dashboard.api.routes_auth import router as router_auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_transacoes)
app.include_router(router_categorias)
app.include_router(router_usuarios)
app.include_router(router_auth)