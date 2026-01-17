from pydantic import BaseModel, Field
from app.productos.domain.value_objects.nombre_producto import NombreProducto
from app.productos.domain.value_objects.precio_producto import PrecioProducto

class Producto(BaseModel):
    id :int = Field(..., description="Id producto")
    nombre : NombreProducto
    descripcion:str
    precio : PrecioProducto
    activo : bool
    imagen : str
    stock : int