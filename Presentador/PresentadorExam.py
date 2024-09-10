from Vista.GestionarExam import GestionarExam
from Vista.AgregarExamGen import AgregarExamGen
from Vista.ActualizarExamGen import ActualizarExamGen
from Modelo.ExamenGen import ExamenGen
from Presentador.PresentadorPregGen import PresentadorPregGen

class PresentadorExam:
    def __init__(self, rep, vista_princ):
        self.__rep = rep
        self.__vista_princ = vista_princ

#-----------Ventana Gestionar Exámenes----------------------------------------------------
    def iniciar(self):
        self.__vista = GestionarExam(self)
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def cargarDatos(self):
        self.__vista.desactivarBtnEdicion()
        self.__exam_gen = self.__rep.obtenerExamGen()
        self.__vista.vaciarTabla()
        for exam in self.__exam_gen:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, exam.obtener_elemento().fecha)
            self.__vista.agregar_elemento_tabla(i, 1, exam.obtener_elemento().asignatura)
            if exam.obtener_elemento().calificado:
                calificado = "SÍ"
            else:
                calificado = "NO"
            self.__vista.agregar_elemento_tabla(i, 2, calificado)
        self.__vista.tabla.resizeColumnsToContents()

    def eliminarExam(self):
        try:
            fila_selec = self.__vista.tabla.currentRow()
            exam_borrar = self.__exam_gen.nodo_en(fila_selec).obtener_elemento()
            selec = self.__vista.mostrarAdvertencia("Al borrar un examen borrará todos los exámenes calificados asociados a este\n¿Está seguro que desea continuar?")
            if selec:
                self.__rep.eliminarExamGen(exam_borrar)
                self.cargarDatos()
        except Exception as error:
            self.__vista.mostrarError(str(error))

    def finalizarCalExam(self):
        try:
            selec = self.__vista.mostrarAdvertencia("Una vez finalizada la calificación de un examen, no se podrá añadir ninguna nueva calificación\n¿Desea continuar?")
            if selec:  
                fila_select = self.__vista.tabla.currentRow()
                exam = self.__exam_gen.nodo_en(fila_select).obtener_elemento()
                exam.calificado = True
                self.__rep.actualizarExamGen(exam, exam)
                self.cargarDatos()
        except Exception as error:
            self.__vista.mostrarError(str(error))
        
    
#----------Ventana Añadir Examen-----------------------------------------------------------
    def agregarExamVentana(self):
        self.__ag_act = AgregarExamGen(self)
        self.__ag_act.show()
        self.__vista.bloquearVentana()

    def agregarExam(self):
        try:
            exam_gen = ExamenGen(self.__ag_act.valor_fecha, self.__ag_act.valor_asignatura, False)
            self.__rep.insertarExamGen(exam_gen)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))

#---------Ventana Actualizar Examen--------------------------------------------------------
    def actualizarExamVentana(self):
        self.__ag_act = ActualizarExamGen(self)
        fila_selec = self.__vista.tabla.currentRow()
        self.__exam_anterior = self.__exam_gen.nodo_en(fila_selec).obtener_elemento()
        self.cargarDatosActualizar(self.__exam_anterior)
        self.__ag_act.show()
        self.__vista.bloquearVentana()

    def cargarDatosActualizar(self, exam_anterior):
        self.__ag_act.valor_fecha = exam_anterior.fecha
        self.__ag_act.valor_asignatura = exam_anterior.asignatura
        if self.__rep.examGenTienePasos(exam_anterior):
            self.__ag_act.desactivar_asignatura_selec()
        else:
            self.__ag_act.activar_asignatura_selec()
        

    def actualizarExam(self):
        try:
            nuevo_exam = ExamenGen(self.__ag_act.valor_fecha, self.__ag_act.valor_asignatura, self.__exam_anterior.calificado)
            self.__rep.actualizarExamGen(self.__exam_anterior, nuevo_exam)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))

#---------------Ventana Configurar Clave--------------------------------------
    def configurarClaveVentana(self):
        try:
            if self.__exam_anterior.calificado:
                raise Exception("La calificación del examen ha terminado, por tanto no se puede modificar su clave")
            elif self.__rep.examGenTieneExamEsp(self.__exam_anterior):
                raise Exception("Ya se han calificado estudiantes de este examen, por tanto no se puede modificar la clave")
            else:
                self.__clave_ventana = PresentadorPregGen(self.__rep, self.__ag_act, self.__exam_anterior)
                self.__clave_ventana.iniciar() 
                self.__ag_act.bloquearVentana()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))
    

