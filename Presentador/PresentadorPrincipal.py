import sys
from PyQt5.QtWidgets import QApplication
from Vista.VentanaPrincipal import VentanaPrincipal
from Modelo.Repositorio import Repositorio
from Presentador.PresentadorExam import PresentadorExam
from Presentador.PresentadorObj import PresentadorObj
from Presentador.PresentadorEst import PresentadorEst

class PresentadorPrincipal:
    def __init__(self):
        self.__rep = Repositorio()

    #Iniciar Ventana Principal
    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal(self)
        self.__vista.show()
        app.exec_()

    #Iniciar Ventana Gestionar Exámenes
    def gestionarExam(self):
        gestionar_exam = PresentadorExam(self.__rep, self.__vista)
        gestionar_exam.iniciar()

    #Iniciar Ventana Gestionar Objetivos
    def gestionarObj(self):
        gestionar_obj = PresentadorObj(self.__rep, self.__vista)
        gestionar_obj.iniciar()

    #Iniciar Ventana Gestionar Estudiantes
    def gestionarEst(self):
        gestionar_est = PresentadorEst(self.__rep, self.__vista)
        gestionar_est.iniciar()
    

        