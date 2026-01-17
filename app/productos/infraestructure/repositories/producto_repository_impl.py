from typing import List, Optional

from app.productos.domain.repository.producto_repository import ProductoRepository
from app.productos.domain.entities.producto import Producto
from app.infraestructure.database.db_connection_factory import DBConnectionFactory

class ProductoRepositoryImpl(ProductoRepository):
    def get_all(self) -> List[Producto]:
        connection = DBConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, descripcion, precio, activo, imagen, stock FROM producto_producto")
                rows = cursor.fetchall()
                productos = [Producto(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], activo=row[4], imagen=row[5], stock=row[6]) for row in rows]
                return productos
        finally:
            DBConnectionFactory.release_connection(connection)
    
    def get_by_id(self, producto_id: int) -> Optional[Producto]:
        connection = DBConnectionFactory.get_connection()
        try:
           pass
        finally:
            DBConnectionFactory.release_connection(connection)

    def create (self, producto:Producto) -> Producto:
        connection = DBConnectionFactory.get_connection()
        try:
            pass
        finally:
            DBConnectionFactory.release_connection(connection)

    def update(self, producto_id:int ,producto:Producto) -> Optional[Producto]:
        connection = DBConnectionFactory.get_connection()
        try:
            pass
        finally:
            DBConnectionFactory.release_connection(connection)

    def delete(self, producto_id: int) -> bool:
        connection = DBConnectionFactory.get_connection()
        try:
            pass
        finally:
            DBConnectionFactory.release_connection(connection)
