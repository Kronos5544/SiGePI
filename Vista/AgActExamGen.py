from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate

class AgActExamGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/AgActExamGen.ui", self)

        self.asignatura_selec.addItems(["Matemática", "Español", "Historia"])
        self.clave_btn.clicked.connect(self.__presentador.configurarClaveVentana)
        self.cancelar_btn.clicked.connect(self.close)

    @property
    def valor_fecha(self):
        return self.fecha_selec.date().toString('yyyy-MM-dd')
    @valor_fecha.setter
    def valor_fecha(self, value):
        value = QDate.fromString(value, "yyyy-MM-dd")
        self.fecha_selec.setDate(value)

    @property
    def valor_asignatura(self):
        return self.asignatura_selec.currentText()
    @valor_asignatura.setter
    def valor_asignatura(self, valor):
        self.asignatura_selec.setCurrentText(valor)

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