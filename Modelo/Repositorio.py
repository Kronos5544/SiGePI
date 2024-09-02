from Modelo.Objetivo import Objetivo
from Modelo.ListaEnlazada import ListaEnlazada
from Modelo.Conexion import Conexion

class Repositorio:
    def __init__(self):
        self.__conexion = Conexion()

#---------CRUD (Create Read Update Delete) de los objetivos---------------------------------------------
    def insertarObj(self, obj):
        """
        Comprueba si el objetivo existe en la tabla Objetivo, de existir lanza un error, de no hacerlo lo inserta
        :param obj: objeto objetivo
        :return: None 
        """

        consulta_comp = f"""
        SELECT "IdObj" From Public."Objetivo" 
        Where "DescObjEsp" = '{obj.desc_obj_esp}' and "Asignatura" = '{obj.asignatura}'
        """
        comp = self.__conexion.cons_un_valor(consulta_comp)

        if comp is None:
            consulta = f"""
            Insert Into Public."Objetivo" 
            Values(default, '{obj.asignatura}', '{obj.desc_obj_esp}', '{obj.desc_obj_gen}')
            """
            self.__conexion.cons_sin_retorno(consulta)
        else:
            raise Exception("El objetivo ya existe")
        
    def obtenerObj(self):
        """
        :return: Lista enlazada con todos los objetivos de la tabla en forma de objetos objetivos
        """

        consulta = """
        Select * From Public."Objetivo"
        """
        listaObj = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for obj in lista:
            objetivo = Objetivo(obj[0], obj[1], obj[2], obj[3])
            listaObj.agregar(objetivo)
        return listaObj
    
    def actualizar_obj(self, obj_anterior, obj):
        """
        :param obj_anterior: Objeto Objetivo al que se desea actualizar
        :param obj: Objeto Objetivo que contiene los cambios a realizar
        :return: None
        """
        
        consulta = f"""
        UPDATE Public."Objetivo"    
        SET "Asignatura" = '{obj.asignatura}' , "DescObjEsp" = '{obj.desc_obj_esp}', "DescObjGen" = '{obj.desc_obj_gen}'
        WHERE "IdObj" = {obj_anterior.id_obj} 
        """
        self.__conexion.cons_sin_retorno(consulta)

    def eliminar_obj(self, obj):
        """
        :param obj: Objeto Objetivo a eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."Objetivo" Where "IdObj" = {obj.id_obj} 
        """
        self.__conexion.cons_sin_retorno(consulta)



