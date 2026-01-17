from typing import Union

from fastapi import FastAPI
from app.productos.infraestructure.routers.producto_router import router as producto_router
from app.infraestructure.database.db_connection_factory import DBConnectionFactory

app = FastAPI(title = "FastAPI - Arquitectura Hexagonal ")

@app.on_event("startup")
def startup():
    DBConnectionFactory.initialize()

@app.on_event("shutdown")
def shutdown():
    print("Cerrando pool de conexiones...")
    DBConnectionFactory.close_pool()

app.include_router(producto_router, prefix="/productos", tags=["Productos"])