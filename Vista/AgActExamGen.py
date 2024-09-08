from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

class AgActExamGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/AgActExamGen.ui", self)

        self.asignatura_selec.addItems(["Matemática", "Español", "Historia"])
        #self.clave_btn.clicked.connect(self.__presentador.seleccionarVentana)
        self.cancelar_btn.clicked.connect(self.close)

    def ocultarClaveBtn(self, valor):
        self.clave_btn.setHidden(valor)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)   

    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error) 

    def closeEvent(self, event):
        self.__presentador.desbloquearVentana()
        self.__presentador.cargarDatos()
        event.accept()