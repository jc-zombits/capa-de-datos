from logger_base import log
from psycopg2 import pool
import sys


class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Jcadmin'
    _DB_PORT = '5432'
    _HOST = '192.168.58.113'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    # Metodo para el pool de conexiones
    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación de pool exitoda {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ha ocurrido un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool

    # Metodo para obtener conexión
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool {conexion}')
        return conexion

    @classmethod
    def librearConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

    # Método para obtener cursor
    #@classmethod
    #def obtenerCursor(cls):
    #    pass


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.librearConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.librearConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.librearConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
