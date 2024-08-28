import psycopg

class Coneccion:
    def __init__(self):
        self.__dir = "dbname=SiGePI user=postgres port=5432 password = Toni2003+"

    def cons_un_valor(self, consulta):
        """
        :param consulta: consulta en formato SQL
        :return: Devuelve una lista con una única fila
        """
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchone()
                return resultado
       
        
    
    def cons_mult_valor(self, consulta):
        """
        :param consulta: consulta en formato SQL
        :return: Devuelve una lista de listas con varias filas
        """
        with psycopg.connect(self.__dir) as conn:
            with conn.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                return resultado