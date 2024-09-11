from Vista.ActualizarExamEsp import ActualizarExamEsp
from Presentador.PresentadorActPasoEsp import PresentadorActPasoEsp

class PresentadorActExamEsp:
    def __init__(self, rep, vista_princ, exam_esp):
        self.__rep = rep
        self.__vista_princ = vista_princ
        self.__exam_esp = exam_esp

    def iniciar(self):
        self.__vista = ActualizarExamEsp(self)
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def cargarDatos(self):
        self.__vista.desactivarBtnEdicion()
        self.__vista.valor_est_id = self.__exam_esp.est_id
        self.__preg_esp = self.__rep.obtenerPreguntaEsp(self.__exam_esp)
        preguntas = self.__rep.unirPregEspPregGen(self.__exam_esp)
        self.__vista.valor_desc_ort = self.__exam_esp.desc_ort
        self.__vista.vaciarTabla()
        for preg in preguntas:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, str(preg[0]))
            self.__vista.agregar_elemento_tabla(i, 1, str(preg[1]))
            self.__vista.agregar_elemento_tabla(i, 2, str(preg[2]))
        self.__vista.tabla.resizeColumnsToContents()


    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()
    
    def editarDescOrt(self):
        try:
            self.__exam_esp.desc_ort = self.__vista.valor_desc_ort
            self.__rep.actualizarExamEsp(self.__exam_esp, self.__exam_esp)
        except Exception as error:
            self.__vista.mostrarError(str(error))

#----------Ventana editar Pasos Específicos------------------------
    def editarCalPregVentana(self):
        preg_esp = self.__preg_esp.nodo_en(self.__vista.tabla.currentRow()).obtener_elemento()
        self.__editar = PresentadorActPasoEsp(self.__rep, self.__vista, preg_esp)
        self.__editar.iniciar()
        self.__vista.bloquearVentana()
    

    