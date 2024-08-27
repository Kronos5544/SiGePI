import psycopg

class Conexion:
    def __init__(self):
        self.__dir = "dbname=SiGePI user=postgres port=5432 password = Toni2003+"

    def consultaSimp(self, consulta):
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchone()
                return resultado
        
    
    def consultaMult(self, consulta):
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                return resultado


e = Conexion()