from abc import ABC, abstractmethod
from typing import List, Optional

from app.productos.domain.entities.producto import Producto

class ProductoRepository(ABC): #Clase abstracta
    @abstractmethod
    def get_all(self) -> List[Producto]: # al aplicar este metodo nos retornara una lista de productos
        pass
    
    @abstractmethod
    def get_by_id(self, producto_id: int) -> Optional[Producto]:
        pass

    @abstractmethod
    def create (self, producto:Producto) -> Producto:
        pass

    @abstractmethod
    def update(self, producto_id:int ,producto:Producto) -> Optional[Producto]:
        pass

    @abstractmethod
    def delete(self, producto_id: int) -> bool:
        pass


