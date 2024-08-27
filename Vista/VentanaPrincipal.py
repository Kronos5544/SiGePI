from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('Vista/ui/VentanaPrincipal.ui', self)

        self.salir_btn.clicked.connect(self.close)
        self.gest_exam_btn.clicked.connect(self.__presentador.gestionarExam)