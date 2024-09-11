from Modelo.Objetivo import Objetivo
from Modelo.ExamenGen import ExamenGen
from Modelo.ExamenEsp import ExamenEsp
from Modelo.PreguntaGen import PreguntaGen
from Modelo.PreguntaEsp import PreguntaEsp
from Modelo.PasoGen import PasoGen
from Modelo.PasoEsp import PasoEsp
from Modelo.Estudiante import Estudiante
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
        WHERE "DescObjEsp" = '{obj.desc_obj_esp}'
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
            examen = ExamenGen(str(exam[0]), exam[1], exam[2])
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
        
    def obtenerExamEsp(self, exam):
        """
        :return: Objeto ListaEnlazada que contiene todos los examenes generales en forma de Objeto ExamenEsp
        """
        consulta = f"""
        SELECT * FROM PUBLIC."ExamenEsp"
        WHERE "Fecha" = '{exam.fecha}'
        """
        
        lista_exam_esp = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for exam in lista:
            examen_esp = ExamenEsp(exam[0], str(exam[1]), exam[2], exam[3])
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
        
    def obtenerPreguntaGen(self, exam):
        """
        :return: Objeto ListaEnlazada que contiene todas las preguntas generales en forma de Objeto PreguntaGen
        """
        consulta = f"""
        SELECT * FROM PUBLIC."Pregunta"
        WHERE "Fecha" = '{exam.fecha}'
        """
        
        lista_preg_gen = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for preg in lista:
            pregunta_gen = PreguntaGen(str(preg[0]), preg[1], preg[2])
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
        
    def obtenerPreguntaEsp(self, exam_esp):
        """
        :return: Objeto ListaEnlazada que contiene todas las preguntas específicas en forma de Objeto PreguntaEsp
        """
        consulta = f"""
        SELECT * FROM PUBLIC."PreguntaEsp"
        WHERE "EstId" = '{exam_esp.est_id}' AND "Fecha" = '{exam_esp.fecha}'
        ORDER BY "NoPregunta" ASC
        """
        
        lista_preg_esp = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for preg in lista:
            pregunta_esp = PreguntaEsp(str(preg[0]), preg[1], preg[2], preg[3])
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
        Comprueba si el paso existe en la tabla y de existir, no la inserta, de lo contrario la inserta
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
        
    def obtenerPasoGen(self, pregunta, variante):
        """
        :return: Objeto ListaEnlazada que contiene todos los pasos generales en forma de Objeto PasoGen
        """
        consulta = f"""
        SELECT * FROM PUBLIC."Paso"
        WHERE "Fecha" = '{pregunta.fecha}' AND "NoPregunta" = {pregunta.no_pregunta} AND "Variante" = '{variante}'
        """
        
        lista_paso_gen = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for paso in lista:
            paso_gen = PasoGen(paso[0], paso[1], paso[2], str(paso[3]), paso[4], paso[5])
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
        :param paso: Objeto PasoEsp que representa el paso que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."Paso"
        WHERE "NoPaso" = {paso.no_paso} AND "Variante" = '{paso.variante}' AND "NoPregunta" = {paso.no_pregunta} AND "Fecha" = '{paso.fecha}'
        """
        self.__conexion.cons_sin_retorno(consulta)

    
    def insertarPasoEsp(self, paso):
        """
        Comprueba si el paso existe en la tabla y de existir, no la inserta, de lo contrario la inserta
        :param paso: Objeto PasoEsp a insertar en la tabla
        :return: None 
        """

        try:
            consulta = f"""
            INSERT INTO PUBLIC."PasoEsp"
            VALUES('{paso.est_id}', '{paso.fecha}', {paso.no_paso}, '{paso.variante}', {paso.no_pregunta}, {paso.calificacion})
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("El paso ya ha sido calificado en este examen")
        
    def obtenerPasoEsp(self, pregunta, variante):
        """
        :return: Objeto ListaEnlazada que contiene todos los pasos específicos en forma de Objeto PasoEsp
        """
        consulta = f"""
        SELECT * FROM PUBLIC."PasoEsp"
        WHERE "Fecha" = '{pregunta.fecha}' AND "NoPregunta" = '{pregunta.no_pregunta}' AND "EstId" = '{pregunta.est_id}' AND "Variante" = '{variante}'
        ORDER BY "NoPaso" ASC
        """
        
        lista_paso_esp = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for paso in lista:
            paso_esp = PasoEsp(paso[0], str(paso[1]), paso[2], paso[3], paso[4], paso[5])
            lista_paso_esp.agregar(paso_esp)
        return lista_paso_esp
    
    def actualizarPasoEsp(self, paso_anterior, paso):
        """
        :param paso_anterior: Objeto PasoEsp que representa el paso que se quiere actualizar
        :param paso: Objeto PasoEsp que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE PUBLIC."PasoEsp"
            SET "Calificacion" = {paso.calificacion}
            WHERE "EstId" = '{paso_anterior.est_id}' AND "Fecha" = '{paso_anterior.fecha}' AND "NoPaso" = {paso_anterior.no_paso} AND "Variante" = '{paso_anterior.variante}' AND "NoPregunta" = {paso_anterior.no_pregunta}
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe otro paso con los mismos datos")
        
    def eliminarPasoEsp(self, paso):
        """
        :param paso: Objeto PasoEsp que representa el paso que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM PUBLIC."PasoEsp"
        WHERE "EstId" = '{paso.est_id}' AND "Fecha" = '{paso.fecha}' AND "NoPaso" = {paso.no_paso} AND "Variante" = '{paso.variante}' AND "NoPregunta" = {paso.no_pregunta}
        """
        self.__conexion.cons_sin_retorno(consulta)


#------------------CRUD(Create Read Update Delete) de Estudiantes
    def insertarEstudiante(self, estudiante):
        """
        Comprueba si el estudiante existe en la tabla y de existir, no la inserta, de lo contrario la inserta
        :param estudiante: Objeto Estudiante a insertar en la tabla
        :return: None 
        """

        try:
            consulta = f"""
            INSERT INTO public."Estudiante" VALUES ('{estudiante.est_id}') 
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("El estudiante ya existe")
        
    def obtenerEstudiante(self):
        """
        :return: Objeto ListaEnlazada que contiene todos los estudiantes en forma de Objeto Estudiante
        """
        consulta = """
        SELECT * FROM PUBLIC."Estudiante"
        """
        
        lista_estudiante = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for est in lista:
            estudiante = Estudiante(est[0])
            lista_estudiante.agregar(estudiante)
        return lista_estudiante
    
    def actualizarEstudiante(self, est_anterior, est_nuevo):
        """
        :param est_anterior: Objeto Estudiante que representa el estudiante que se quiere actualizar
        :param est_nuevo: Objeto Estudiante que representa los cambios a realizar
        :return: None
        """

        try:
            consulta = f"""
            UPDATE public."Estudiante"
	        SET "EstId"= '{est_nuevo.est_id}'
	        WHERE "EstId" = '{est_anterior.est_id}'
            """
            self.__conexion.cons_sin_retorno(consulta)
        except UniqueViolation:
            raise Exception("Ya existe otro estudiante con la misma Id")
    
    def eliminarEstudiante(self, estudiante):
        """
        :param estudiante: Objeto Estudiante que representa el estudiante que se quiere eliminar
        :return: None
        """

        consulta = f"""
        DELETE FROM public."Estudiante"
	    WHERE "EstId" = '{estudiante.est_id}'
        """
        self.__conexion.cons_sin_retorno(consulta)

    
#--------------Métodos útiles----------------------------------------------------------------
    def objetivoGenXAsig(self, asignatura):
        consulta = f"""
        SELECT "DescObjGen" FROM Public."Objetivo" WHERE "Asignatura" = '{asignatura}'
        """ 
        lista_obj_gen = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)

        if lista is not None:
            for obj_gen in lista:
                lista_obj_gen.agregar(obj_gen[0])

        return lista_obj_gen
    
    def examGenTieneExamEsp(self, examen):
        consulta = f"""
        SELECT * FROM Public."ExamenEsp"
        WHERE "Fecha" = '{examen.fecha}'
        """
        exam = self.__conexion.cons_un_valor(consulta)

        if exam is None:
            return False
        else:
            return True
    
    def compClaveExamGen(self, examen):
        consulta = f"""SELECT comp_clave_exam('{examen.fecha}')"""
        resultado = self.__conexion.cons_un_valor(consulta)
        if True in resultado:
            return True
        else:
            return False
        
    def varianteExamenGen(self, examen):
        consulta = f"""
        SELECT DISTINCT "Variante" FROM Public."Paso"
        WHERE "Fecha" = '{examen.fecha}'
        """

        variantes = self.__conexion.cons_mult_valor(consulta)
        variantes_fin = []

        if len(variantes) == 0:
            variantes_fin = ["A"]
        else:
            for e in variantes:
                variantes_fin.append(e[0])
        
        return variantes_fin

    def variantePreg(self, preg):
        consulta = f"""
        SELECT DISTINCT "Variante" FROM Public."Paso"
        WHERE "Fecha" = '{preg.fecha}' AND "NoPregunta" = {preg.no_pregunta}
        """

        variantes = self.__conexion.cons_mult_valor(consulta)
        variantes_fin = []

        if len(variantes) == 0:
            variantes_fin = ["A"]
        else:
            for e in variantes:
                variantes_fin.append(e[0])
        
        return variantes_fin
    
    def compVariante(self, preg, variante):
        consulta = f"""
        SELECT comp_clave_preg_x_var('{preg.fecha}', {preg.no_pregunta}, '{variante}')
        """

        comp = self.__conexion.cons_un_valor(consulta)
        
        if True in comp:
            comp = "OK"
        else:
            comp = "INC"
        return comp
    
    def calcCalExamGen(self, exam):
        consulta = f"""
        SELECT SUM("MaxCal") FROM Public."Pregunta"
        WHERE "Fecha" = '{exam.fecha}'
        """
        resultado = self.__conexion.cons_un_valor(consulta)
        if None in resultado:
            return 0
        return resultado[0]
    
    def compCalExamenGen(self, exam):
        consulta = f"""
        SELECT comp_cal_exam('{exam.fecha}')
        """
        if True in self.__conexion.cons_un_valor(consulta):
            return True
        else:
            return False
        
    def unirPasoGenObj(self, preg, var):
        consulta = f"""
        SELECT "NoPaso", "MaxCal", "DescObjEsp", "DescObjGen"
        FROM (SELECT * FROM Public."Paso" WHERE "Fecha" = '{preg.fecha}' AND "NoPregunta" = {preg.no_pregunta} AND "Variante" = '{var}') AS "Pasos"
        JOIN Public."Objetivo" ON "Pasos"."IdObj" = "Objetivo"."IdObj"
        ORDER BY "NoPaso" ASC
        """
        
        cons = self.__conexion.cons_mult_valor(consulta)
        tabla = ListaEnlazada()

        for e in cons:
            tabla.agregar(e)

        return tabla
    
    def calcCalPreg(self, preg, var):
        consulta = f"""
        SELECT SUM("MaxCal") FROM Public."Paso"
        WHERE "Fecha" = '{preg.fecha}' AND "NoPregunta" = {preg.no_pregunta} AND "Variante" = '{var}'
        """
        resultado = self.__conexion.cons_un_valor(consulta)
        if None in resultado:
            return 0
        return resultado[0]
    
    def obtenerAsigExam(self, fecha):
        consulta = f"""
        SELECT "Asignatura" FROM Public."Examen"
        WHERE "Fecha" = '{fecha}'
        """
        resultado = self.__conexion.cons_un_valor(consulta)

        return resultado[0]
    
    def obtenerObjXAsig(self, asig):
        consulta = f"""
        SELECT * FROM Public."Objetivo"
        WHERE "Asignatura" = '{asig}'
        ORDER BY "IdObj" ASC
        """

        listaObj = ListaEnlazada()
        lista = self.__conexion.cons_mult_valor(consulta)
        for obj in lista:
            objetivo = Objetivo(obj[0], obj[1], obj[2], obj[3])
            listaObj.agregar(objetivo)
        return listaObj
    
    def examGenTienePasos(self, exam):
        consulta = f"""
        SELECT * FROM Public."Paso"
        WHERE "Fecha" = '{exam.fecha}'
        """
        
        resultado = self.__conexion.cons_un_valor(consulta)

        if resultado != None:
            return True
        else:
            return False
        
    def unirPregEspPregGen(self, exam_esp):
        consulta = f"""
        SELECT "PreguntaEsp"."NoPregunta", "Calificacion", "MaxCal" FROM Public."PreguntaEsp"
        JOIN Public."Pregunta" ON "Pregunta"."NoPregunta" = "PreguntaEsp"."NoPregunta" 
        AND "Pregunta"."Fecha" = "PreguntaEsp"."Fecha"
        WHERE "PreguntaEsp"."Fecha" = '{exam_esp.fecha}' AND "PreguntaEsp"."EstId" = '{exam_esp.est_id}'
        ORDER BY "PreguntaEsp"."NoPregunta" ASC
        """

        return self.__conexion.cons_mult_valor(consulta)
    
    def obtenerVarPregEsp(self, preg_esp):
        consulta = f"""
        SELECT "Variante" FROM Public."PasoEsp"
        WHERE "NoPregunta" = {preg_esp.no_pregunta} AND "Fecha" = '{preg_esp.fecha}' AND "EstId" = '{preg_esp.est_id}'
        """

        return self.__conexion.cons_un_valor(consulta)[0]
    
    def unirPasoEspGenObj(self, preg_esp, var):
        consulta = f"""
        SELECT "PasoEsp"."NoPaso", "Calificacion", "MaxCal", "DescObjEsp", "DescObjGen" FROM Public."PasoEsp"
        JOIN Public."Paso" ON "Paso"."NoPregunta" = "PasoEsp"."NoPregunta" AND "PasoEsp"."Variante" = "Paso"."Variante" AND "PasoEsp"."NoPaso" = "Paso"."NoPaso" AND "PasoEsp"."Fecha" = "Paso"."Fecha"
        JOIN Public."Objetivo" ON "Paso"."IdObj" = "Objetivo"."IdObj"
        WHERE "EstId" = '{preg_esp.est_id}' AND "PasoEsp"."NoPregunta" = {preg_esp.no_pregunta} AND "PasoEsp"."Fecha" = '{preg_esp.fecha}' AND "PasoEsp"."Variante" = '{var}'
        ORDER BY "PasoEsp"."NoPaso" ASC
        """

        return self.__conexion.cons_mult_valor(consulta)
    

        
