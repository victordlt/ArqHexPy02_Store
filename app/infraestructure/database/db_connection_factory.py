# basado en patron Factory y Patron Singleton
from psycopg2 import pool

class DBConnectionFactory:
    _connection_pool = None
    
    @classmethod
    def initialize(cls, minconn:int = 1, maxconn:int=5):
        if cls._connection_pool is None:
            cls._connection_pool = pool.SimpleConnectionPool(
                minconn,
                maxconn,
                user='postgres',
                password='example',
                host='localhost', # la db esta en un contendor docker
                port='5432',
                database='postgres'
            )
    
    @classmethod
    def get_connection(cls):
        if cls._connection_pool is None:
            raise Exception("Pool de conexiones no inicializado. Llame a 'initialize' primero.")
        return cls._connection_pool.getconn()
    
    @classmethod
    def release_connection(cls, connection):
        if cls._connection_pool is None:
            raise Exception("Pool de conexiones no inicializado. Llame a 'initialize' primero.")
        cls._connection_pool.putconn(connection)

    @classmethod
    def close_pool (cls):
        if cls._connection_pool:
            cls._connection_pool.closeall()
            cls._connection_pool = None