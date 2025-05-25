from fastapi import FastAPI
from app.api.v1 import (
    auth_routes, clients, products, orders, whatsapp, orcamentos,
    promocoes, categorias
)
from config.sentry_config import init_sentry

init_sentry()  

app = FastAPI(title="Lu Estilo API", version="1.0.0")

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(whatsapp.router, tags=["whatsapp"])
app.include_router(orcamentos.router, prefix="/orcamentos", tags=["orcamentos"])
app.include_router(promocoes.router, prefix="/promocoes", tags=["promoções"])
app.include_router(categorias.router, prefix="/categorias", tags=["categorias"])

@app.get("/")
def root():
    return {"message": "Lu Estilo API online"}
