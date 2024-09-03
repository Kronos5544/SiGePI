from Modelo.Objetivo import Objetivo
from Modelo.ExamenGen import ExamenGen
from Modelo.ExamenEsp import ExamenEsp
from Modelo.PreguntaGen import PreguntaGen
from Modelo.PreguntaEsp import PreguntaEsp
from Modelo.PasoGen import PasoGen
from Modelo.PasoEsp import PasoEsp
from Modelo.ListaEnlazada import ListaEnlazada
from Modelo.Conexion import Conexion
from psycopg.errors import UniqueViolation

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
    
    def actualizarObj(self, obj):
        """
        :param obj: Objeto Objetivo que contiene los cambios a realizar
        :return: None
        """
        
        consulta = f"""
        SELECT "IdObj" FROM Public."Objetivo"
        WHERE "DescObjEsp" = {obj.desc_obj_esp}
        """

        existe = False
        comp = self.__conexion.cons_mult_valor(consulta)

        if comp is None:
            raise Exception("El Objetivo a actualizar no existe")
        else:
            for id in comp:
                if id != obj.id_obj:
                    existe = True

        if not existe:
            consulta = f"""
            UPDATE Public."Objetivo"    
            SET "Asignatura" = '{obj.asignatura}' , "DescObjEsp" = '{obj.desc_obj_esp}', "DescObjGen" = '{obj.desc_obj_gen}'
            WHERE "IdObj" = {obj.id_obj} 
            """
            self.__conexion.cons_sin_retorno(consulta)
        else:
            raise Exception("Ya existe un objetivo con la misma descripción de objetivo específico")

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
        """
        Comprueba si el examen existe en la tabla antes de insertarlo y de existir lanza un error
        :param examen: Objeto ExamenGen que se desea insertar en la tabla Examen
        :return: None
        """

        try:
            consulta = f"""
            INSERT INTO Public."Examen" 
            VALUES ('{examen.fecha}', '{examen.asignatura}', default)
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("El examen a insertar ya existe")
        
    def obtenerExamGen(self):
        """
        :return: Objeto ListaEnlazada que contiene todos los examenes generales en forma de Objeto Examen
        """
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
        """
        :param exam_anterior: Objeto ExamenGen que representa el examen que se quiere actualizar
        :param exam: Objeto ExamenaGen que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE PUBLIC."Examen"
            SET "Fecha" = '{exam.fecha}', "Asignatura" = '{exam.asignatura}', "Calificado" = {exam.calificado}
            WHERE "Fecha" = '{exam_anterior.fecha}'
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe otro examen con la misma fecha")

    def eliminarExamGen(self, exam):
        """
        :param exam: Objeto ExamenGen que representa el examen que se quiere eliminar
        :return: None
        """
        consulta = f"""
        DELETE FROM Public."Examen" 
        WHERE "Fecha" = '{exam.fecha}'
        """
        self.__conexion.cons_sin_retorno(consulta)

    def insertarExamEsp(self, exam):
        """
        Comprueba si el examen existe en la tabla y de existir, no lo inserta, de lo contrario lo inserta
        :param exam: Objeto ExamenEsp a insertar en la tabla
        :return: None 
        """

        try:
            consulta = f"""
            INSERT INTO PUBLIC."ExamenEsp"
            VALUES('{exam.est_id}', '{exam.fecha}', {exam.calificacion}, {exam.desc_ort})
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("El estudiante ya ha sido calificado en este examen")
        
    def obtenerExamEsp(self):
        """
        :return: Objeto ListaEnlazada que contiene todos los examenes generales en forma de Objeto ExamenEsp
        """
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
        """
        :param exam_anterior: Objeto ExamenEsp que representa el examen que se quiere actualizar
        :param exam: Objeto ExamenaEsp que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE PUBLIC."ExamenEsp"
            SET "EstId" = '{exam.est_id}', "Calificacion" = {exam.calificacion}, "DescOrt" = {exam.desc_ort}
            WHERE "EstId" = '{exam_anterior.est_id}' AND "Fecha" = '{exam_anterior.fecha}'
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe otro estudiante con el mismo ID")

    def eliminarExamEsp(self, exam):
        """
        :param exam: Objeto ExamenEsp que representa el examen que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."ExamenEsp"
        WHERE "Fecha" = '{exam.fecha}' AND "EstId" = '{exam.est_id}'
        """
        self.__conexion.cons_sin_retorno(consulta)



#--------------------------CRUD(Create, Read, Update) de las preguntas-------------------------------------------------
    def insertarPreguntaGen(self, pregunta):
        """
        Comprueba si la pregunta existe en la tabla y de existir, no la inserta, de lo contrario la inserta
        :param pregunta: Objeto PreguntaGen a insertar en la tabla
        :return: None 
        """

        try:
            consulta = f"""
            INSERT INTO PUBLIC."Pregunta"
            VALUES('{pregunta.fecha}', '{pregunta.no_pregunta}', {pregunta.max_cal})
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("La Pregunta ya existe")
        
    def obtenerPreguntaGen(self):
        """
        :return: Objeto ListaEnlazada que contiene todas las preguntas generales en forma de Objeto PreguntaGen
        """
        consulta = """
        SELECT * FROM PUBLIC."Pregunta"
        """
        
        lista_preg_gen = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for preg in lista:
            pregunta_gen = PreguntaGen(preg[0], preg[1], preg[2])
            lista_preg_gen.agregar(pregunta_gen)
        return lista_preg_gen
    
    def actualizarPregGen(self, preg_anterior, pregunta):
        """
        :param preg_anterior: Objeto PreguntaGen que representa la pregunta que se quiere actualizar
        :param pregunta: Objeto PreguntaGen que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE PUBLIC."Pregunta"
            SET "NoPregunta" = {pregunta.no_pregunta}, "MaxCal" = {pregunta.max_cal}
            WHERE "NoPregunta" = {preg_anterior.no_pregunta} AND "Fecha" = '{preg_anterior.fecha}'
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe una pregunta con la misma fecha y No pregunta")
        
    def eliminarPregGen(self, pregunta):
        """
        :param pregunta: Objeto PreguntaGen que representa la pregunta que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."Pregunta"
        WHERE "Fecha" = '{pregunta.fecha}' AND "NoPregunta" = {pregunta.no_pregunta}
        """
        self.__conexion.cons_sin_retorno(consulta)

    def insertarPreguntaEsp(self, pregunta):
        """
        Comprueba si la pregunta existe en la tabla y de existir, no la inserta, de lo contrario la inserta
        :param pregunta: Objeto PreguntaEsp a insertar en la tabla
        :return: None 
        """

        try:
            consulta = f"""
            INSERT INTO PUBLIC."PreguntaEsp"
            VALUES('{pregunta.fecha}', '{pregunta.est_id}' ,{pregunta.no_pregunta}, {pregunta.calificacion})
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("La Pregunta ya existe")
        
    def obtenerPreguntaEsp(self):
        """
        :return: Objeto ListaEnlazada que contiene todas las preguntas específicas en forma de Objeto PreguntaEsp
        """
        consulta = """
        SELECT * FROM PUBLIC."PreguntaEsp"
        """
        
        lista_preg_esp = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for preg in lista:
            pregunta_esp = PreguntaEsp(preg[0], preg[1], preg[2], preg[3])
            lista_preg_esp.agregar(pregunta_esp)
        return lista_preg_esp
    
    def actualizarPregEsp(self, preg_anterior, pregunta):
        """
        :param preg_anterior: Objeto PreguntaEsp que representa la pregunta que se quiere actualizar
        :param pregunta: Objeto PreguntaEsp que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE PUBLIC."PreguntaEsp"
            SET "Calificacion" = {pregunta.calificacion}
            WHERE "Fecha" = '{preg_anterior.fecha}' AND "EstId" = '{preg_anterior.est_id}' AND "NoPregunta" = {preg_anterior.no_pregunta}
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe una pregunta calificada con los mismos datos")
    
    def eliminarPregEsp(self, pregunta):
        """
        :param pregunta: Objeto PreguntaEsp que representa el examen que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."PreguntaEsp"
        WHERE "Fecha" = '{pregunta.fecha}' AND "NoPregunta" = {pregunta.no_pregunta} AND "EstId" = '{pregunta.est_id}'
        """
        self.__conexion.cons_sin_retorno(consulta)



#-----------------------CRUD(Create Read Update Delete) de los Pasos---------------------------------------------

    def insertarPasoGen(self, paso):
        """
        Comprueba si la pregunta existe en la tabla y de existir, no la inserta, de lo contrario la inserta
        :param paso: Objeto PasoGen a insertar en la tabla
        :return: None 
        """

        try:
            consulta = f"""
            INSERT INTO PUBLIC."Paso"
            VALUES({paso.no_paso}, '{paso.variante}', {paso.no_pregunta}, '{paso.fecha}', {paso.max_cal}, {paso.id_obj})
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("El paso ya existe")
        
    def obtenerPasoGen(self):
        """
        :return: Objeto ListaEnlazada que contiene todos los pasos generales en forma de Objeto PasoGen
        """
        consulta = """
        SELECT * FROM PUBLIC."Paso"
        """
        
        lista_paso_gen = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for paso in lista:
            paso_gen = PasoGen(paso[0], paso[1], paso[2], paso[3], paso[4], paso[5])
            lista_paso_gen.agregar(paso_gen)
        return lista_paso_gen
    
    def actualizarPasoGen(self, paso_anterior, paso):
        """
        :param paso_anterior: Objeto PasoGen que representa el paso que se quiere actualizar
        :param paso: Objeto PasoGen que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE PUBLIC."Paso"
            SET "MaxCal" = {paso.max_cal}, "IdObj" = {paso.id_obj}
            WHERE "Fecha" = '{paso_anterior.fecha}' AND "Variante" = '{paso_anterior.variante}' AND "NoPregunta" = {paso_anterior.no_pregunta} AND "NoPaso" = {paso.no_paso}
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe otro paso con los mismos datos")
        
    def eliminarPasoGen(self, paso):
        """
        :param paso: Objeto Paso que representa el paso que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."Paso"
        WHERE "NoPaso" = {paso.no_paso} AND "Variante" = '{paso.variante}' AND "NoPregunta" = {paso.no_pregunta} AND "Fecha" = '{paso.fecha}'
        """
        self.__conexion.cons_sin_retorno(consulta)