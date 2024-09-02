from Modelo.Objetivo import Objetivo
from Modelo.ExamenGen import ExamenGen
from Modelo.ExamenEsp import ExamenEsp
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
    
    def actualizarObj(self, obj_anterior, obj):
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

    def eliminarObj(self, obj):
        """
        :param obj: Objeto Objetivo a eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."Objetivo" Where "IdObj" = {obj.id_obj} 
        """
        self.__conexion.cons_sin_retorno(consulta)

#------------CRUD (Create Read Update Delete) de las clases Examenes------------------------------
    def insertarExamGen(self, examen):
        consulta = f"""
        SELECT * FROM PUBLIC."Examen" WHERE "Fecha" = '{examen.fecha}'
        """
        comp = self.__conexion.cons_un_valor(consulta)

        if comp is None:
            consulta = f"""
            INSERT INTO Public."Examen" 
            VALUES ('{examen.fecha}', '{examen.asignatura}', default)
            """
            self.__conexion.cons_sin_retorno(consulta)
        else:
            raise Exception("El examen ya existe")
        
    def obtenerExamGen(self):
        consulta = f"""
        SELECT * FROM Public."Examen"
        """
        lista_exam_gen = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for exam in lista:
            examen = ExamenGen(exam[0], exam[1], exam[2])
            lista_exam_gen.agregar(examen)
        return lista_exam_gen
    
    def actualizarExamGen(self, exam_anterior, exam):
        consulta = f"""
        UPDATE PUBLIC."Examen"
        SET "Fecha" = '{exam.fecha}', "Asignatura" = '{exam.asignatura}', "Calificado" = {exam.calificado}
        WHERE "Fecha" = '{exam_anterior.fecha}'
        """
        self.__conexion.cons_sin_retorno(consulta)

    def eliminarExamGen(self, exam):
        consulta = f"""
        DELETE FROM Public."Examen" 
        WHERE "Fecha" = '{exam.fecha}'
        """
        self.__conexion.cons_sin_retorno(consulta)

    def insertarExamEsp(self, exam):
        consulta = f"""
        SELECT * FROM "ExamenEsp" WHERE "EstId" = '{exam.est_id}' AND "Fecha" = '{exam.fecha}'
        """
        comp = self.__conexion.cons_un_valor(consulta)
        if comp is None:
            consulta = f"""
            INSERT INTO PUBLIC."ExamenEsp"
            VALUES('{exam.est_id}', '{exam.fecha}', {exam.calificacion}, {exam.desc_ort})
            """
            self.__conexion.cons_sin_retorno(consulta)
        else:
            raise Exception("El estudiante ya ha sido calificado en este examen")
        
    def obtenerExamEsp(self):
        consulta = """
        SELECT * FROM PUBLIC."ExamenEsp"
        """
        
        lista_exam_esp = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for exam in lista:
            examen_esp = ExamenEsp(exam[0], exam[1], exam[2], exam[3])
            lista_exam_esp.agregar(examen_esp)
        return lista_exam_esp


    def actualizarExamEsp(self, exam_anterior, exam):
        consulta = f"""
        UPDATE PUBLIC."ExamenEsp"
        SET "EstId" = '{exam.est_id}', "Calificacion" = {exam.calificacion}, "DescOrt" = {exam.desc_ort}
        WHERE "EstId" = '{exam_anterior.est_id}' AND "Fecha" = '{exam_anterior.fecha}'
        """
        self.__conexion.cons_sin_retorno(consulta)

    def eliminarExamEsp(self, exam):
        consulta = f"""
        DELETE FROM PUBLIC."ExamenEsp"
        WHERE "Fecha" = '{exam.fecha}' AND "EstId" = '{exam.est_id}'
        """
        
        self.__conexion.cons_sin_retorno(consulta)


