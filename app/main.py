from fastapi import FastAPI
from app.api.v1 import auth_routes, clients, products, orders

app = FastAPI(title="Lu Estilo API", version="1.0.0")

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/")
def root():
    return {"message": "Lu Estilo API online"}
