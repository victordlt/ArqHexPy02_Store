from app.productos.domain.repository.producto_repository import ProductoRepository
from app.productos.domain.entities.producto import Producto

class ProductoService:
    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository

    def get_all(self)-> list[Producto]:
        return self.producto_repository.get_all()

    def get_by_id(self, producto_id: int)-> Producto:
        return self.producto_repository.get_by_id(producto_id)

    def create(self, producto: Producto)-> Producto:
        return self.producto_repository.create(producto)

    def update(self, producto_id: int, producto: Producto)-> Producto:
        return self.producto_repository.update(producto_id, producto)

    def delete(self, producto_id: int) -> bool:
        return self.producto_repository.delete(producto_id)
    

#Aqui tbn se puede agregar logica, es decir un filtrado u operacion matematica.

    