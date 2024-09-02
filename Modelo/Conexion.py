import psycopg

class Conexion:
    def __init__(self):
        self.__dir = "dbname=SiGePI user=postgres port=5432 password = Toni2003+"

    def cons_sin_retorno(self, consulta):
        """
        :param consulta: consulta en formato SQL
        :return:
        """
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)


    def cons_un_valor(self, consulta):
        """
        :param consulta: consulta en formato SQL
        :return: Devuelve una tupla representando una única fila
        """
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchone()
                return resultado
       
        
    def cons_mult_valor(self, consulta):
        """
        :param consulta: consulta en formato SQL
        :return: Devuelve una lista de tuplas que representan cada fila de la tabla
        """
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                return resultado