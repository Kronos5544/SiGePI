import sys
from PyQt5.QtWidgets import QApplication
from Vista.VentanaPrincipal import VentanaPrincipal
from Presentador.PresentadorExam import PresentadorExam

class PresentadorPrincipal:
    def __init__(self):
        pass

    #Iniciar Ventana Principal
    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal(self)
        self.__vista.show()
        app.exec()

    #Iniciar Ventana Gestionar Exámenes
    def gestionarExam(self):
        gestionar_exam = PresentadorExam()
        gestionar_exam.iniciar()


        