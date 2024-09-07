from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('Vista/ui/VentanaPrincipal.ui', self)
        self.setWindowTitle("SiGePI")

        self.salir_btn.clicked.connect(self.close)
        self.gest_exam_btn.clicked.connect(self.__presentador.gestionarExam)
        self.gest_obj_btn.clicked.connect(self.__presentador.gestionarObj)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)

    def closeEvent(self, event):
        if self.isEnabled():
            event.accept()
        else:
            event.ignore()
        