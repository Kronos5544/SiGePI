from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

class AgActPregGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/AgActPregGen.ui", self)

        self.cancelar_btn.clicked.connect(self.close)

    @property
    def valor_max_cal(self):
        return self.cal_num.value()
    @valor_max_cal.setter
    def valor_max_cal(self, value):
        self.cal_num.setValue(value)

    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def restablecerValores(self):
        self.valor_max_cal = 0
    
    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True) 

    def validarDatos(self):
        if self.valor_max_cal <= 0:
            raise Exception("La califiación máxima no puede ser 0")

    def closeEvent(self, event):
        self.__presentador.desbloquearVentana()
        self.__presentador.cargarDatos()
        event.accept()   

    