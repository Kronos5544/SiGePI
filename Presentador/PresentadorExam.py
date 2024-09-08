from Vista.GestionarExam import GestionarExam
from Vista.AgregarExamGen import AgregarExamGen

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
            self.__vista.agregar_elemento_tabla(i, 2, exam.obtener_elemento().calificado)
        self.__vista.tabla.resizeColumnsToContents()
    
#----------Ventana Añadir Examen-----------------------------------------------------------
    def agregarExamVentana(self):
        self.__ag_act = AgregarExamGen(self)
        self.__ag_act.show()
        self.__vista.bloquearVentana()


