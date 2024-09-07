from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

class AgActObj(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/AgActObj.ui", self)

        self.asignatura_selec.addItems(["Matemática", "Español", "Historia"])
        self.selec_btn.clicked.connect(self.__presentador.seleccionarVentana)
        self.cancelar_btn.clicked.connect(self.close)

     
    @property
    def valor_obj_esp(self):
        return self.obj_esp_text.text().strip().capitalize()
    @valor_obj_esp.setter
    def valor_obj_esp(self, valor):
        self.obj_esp_text.setText(valor)

    @property
    def valor_obj_gen(self):
        return self.obj_gen_text.text()
    @valor_obj_gen.setter
    def valor_obj_gen(self, valor):
        self.obj_gen_text.setText(valor)

    @property
    def valor_asignatura(self):
        return self.asignatura_selec.currentText()
    @valor_asignatura.setter
    def valor_asignatura(self, valor):
        self.asignatura_selec.setCurrentText(valor)
    
    
    def validarDatos(self):
        if len(self.valor_obj_esp) == 0:
            raise Exception("El objetivo Específico no puede estar vacío")
        elif len(self.valor_obj_gen) == 0:
            raise Exception("El Objetivo General no puede estar vacío")
        
    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def restablecerValores(self):
        self.valor_obj_esp = ""
        self.valor_obj_gen = ""
    
    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)    
    
    def closeEvent(self, event):
        self.__presentador.desbloquearVentana()
        self.__presentador.cargarDatos()
        event.accept()
