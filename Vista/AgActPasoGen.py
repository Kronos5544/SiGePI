from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

class AgActPasoGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/AgActPasoGen.ui", self)

        self.cancelar_btn.clicked.connect(self.close)
        self.selec_btn.clicked.connect(self.__presentador.selecVentana)

    @property
    def valor_max_cal(self):
        return self.cal_num.value()
    @valor_max_cal.setter
    def valor_max_cal(self, value):
        self.cal_num.setValue(value)

    @property
    def valor_id_obj(self):
        return self.id_obj_text.text()
    @valor_id_obj.setter
    def valor_id_obj(self, valor):
        self.id_obj_text.setText(str(valor))

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
        elif len(self.valor_id_obj) == 0:
            raise Exception("La id del objetivo no puede estar vacía")

    def closeEvent(self, event):
        self.__presentador.desbloquearVentana()
        self.__presentador.cargarDatos()
        event.accept()   