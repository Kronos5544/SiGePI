from Vista.GestionarExamEsp import GestionarExamEsp
from Vista.Seleccion import Seleccion
from Modelo.ExamenEsp import ExamenEsp
from Modelo.PreguntaEsp import PreguntaEsp
from Modelo.PasoEsp import PasoEsp
from Presentador.PresentadorEst import PresentadorEst
from Presentador.PresentadorActExamEsp import PresentadorActExamEsp

class PresentadorExamEsp:
    def __init__(self, rep, vista_princ, examen):
        self.__rep = rep
        self.__vista_princ = vista_princ
        self.__exam = examen

    def iniciar(self):
        self.__vista = GestionarExamEsp(self)
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def cargarDatos(self):
        self.__vista.desactivarBtnEdicion()
        self.__exam_esp = self.__rep.obtenerExamEsp(self.__exam)
        self.__vista.vaciarTabla()
        conf = ["ID Estudiante", "Calificación", "Máx Calificación", "Descuento Ortográfico"]
        self.__vista.configurarTabla(conf)
        for exam in self.__exam_esp:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, str(exam.obtener_elemento().est_id))
            self.__vista.agregar_elemento_tabla(i, 1, str(exam.obtener_elemento().calificacion))
            self.__vista.agregar_elemento_tabla(i, 2, "100")
            self.__vista.agregar_elemento_tabla(i, 3, str(exam.obtener_elemento().desc_ort))
        self.__vista.tabla.resizeColumnsToContents()
    
    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def permitirEdicion(self):
        if self.__exam.calificado:
            return False
        else:
            return True


    def eliminarExamenEsp(self):
        fila_selec = self.__vista.tabla.currentRow()
        self.__rep.eliminarExamEsp(self.__exam_esp.nodo_en(fila_selec).obtener_elemento())
        self.cargarDatos()

#-------------------Ventana selec---------------------------
    def selecVentana(self):
        self.__selec = Seleccion(self)
        self.cargarDatosSelec()
        self.__selec.show()

    def cargarDatosSelec(self):
        try:
            self.__selec.desactivarBtnSelec()
            self.__selec.configurarNombreVentana("Seleccionar Estudiante")
            self.__selec.confNombAbrirGestorBtn("Gestor Estudiantes")
            self.__selec.configurarTabla(["ID Estudiantes"])
            self.__selec.vaciarTabla()
            estudiantes = self.__rep.obtenerEstudiante()
            for est in estudiantes:
                i = self.__selec.tabla.rowCount()
                self.__selec.tabla.insertRow(i)
                self.__selec.agregar_elemento_tabla(i, 0, est.obtener_elemento().est_id)
            self.__selec.tabla.resizeColumnsToContents()
        except Exception as error:
            self.__selec.mostrarError(str(error))
        
    def gestor(self):
        self.__gestor_est = PresentadorEst(self.__rep, self.__vista)
        self.__gestor_est.iniciar()
        self.__selec.close()
        self.__vista.bloquearVentana()
    
    def selec(self):
        try:
            fila_selec = self.__selec.tabla.currentRow()
            exam_esp = ExamenEsp(self.__selec.tabla.item(fila_selec, 0).text(), self.__exam.fecha, 0, 0)
            self.__rep.insertarExamEsp(exam_esp)
            preguntas = self.__rep.obtenerPreguntaGen(self.__exam)
            for preg in preguntas:
                preg_esp = PreguntaEsp(preg.obtener_elemento().fecha, exam_esp.est_id, preg.obtener_elemento().no_pregunta, 0)
                self.__rep.insertarPreguntaEsp(preg_esp)
                pasos = self.__rep.obtenerPasoGen(preg.obtener_elemento(), "A")
                for paso in pasos:
                    paso_esp = PasoEsp(exam_esp.est_id, paso.obtener_elemento().fecha, paso.obtener_elemento().no_paso, "A", paso.obtener_elemento().no_pregunta, 0)
                    self.__rep.insertarPasoEsp(paso_esp)
            self.__selec.close()
            self.cargarDatos()

        except Exception as error:
            self.__selec.mostrarError(str(error))

    def desbVentanaAnterior(self):
        self.__vista.desbloquearVentana()

#---------------Ventana Editar-------------------------
    def editarVentana(self):
        try:
            exam_selec = self.__exam_esp.nodo_en(self.__vista.tabla.currentRow()).obtener_elemento()
            self.__editar = PresentadorActExamEsp(self.__rep, self.__vista, exam_selec)
            self.__editar.iniciar()
            self.__vista.bloquearVentana()
        except Exception as error:
            self.__vista.mostrarError(str(error))