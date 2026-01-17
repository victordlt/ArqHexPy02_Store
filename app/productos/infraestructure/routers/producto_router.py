# Aqui van a aestar nuestro controladores
from fastapi import APIRouter, Depends

from app.productos.infraestructure.repositories.producto_repository_impl import ProductoRepositoryImpl
from app.productos.application.services.producto_service import ProductoService
from app.productos.domain.entities.producto import Producto

from typing import List

router = APIRouter()

def get_producto_service():
    repository = ProductoRepositoryImpl()
    return ProductoService (repository)

@router.get("/", response_model=List[Producto], summary="Obtener todos los productos")
def obtener_productos(service: ProductoService = Depends(get_producto_service)):
    return service.get_all()
