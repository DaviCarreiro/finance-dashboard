from fastapi import FastAPI

from finance_dashboard.api.routes_transacoes import router as router_transacoes

app = FastAPI()

app.include_router(router_transacoes)