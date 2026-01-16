from pydantic import BaseModel, Field

class Producto(BaseModel):
    id :int = Field(..., description="Id producto")
    nombre :str
    descripcion:str
    precio : float
    activo : bool
    imagen : str
    stock : int



