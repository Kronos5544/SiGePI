from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class GestionarExam(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('./Vista/ui/GestionarExam.ui', self)
