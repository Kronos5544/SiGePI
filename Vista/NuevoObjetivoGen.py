from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

class NuevoObjetivoGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/NuevoObjetivoGen.ui", self)
        
        self.aceptar_btn.clicked.connect(self.__presentador.agregarNuevoObjGen)
        self.cancelar_btn.clicked.connect(self.close)
    
    @property
    def valor_obj_gen(self):
        return self.obj_gen_text.text().strip().capitalize()
    @valor_obj_gen.setter
    def valor_obj_gen(self, valor):
        self.obj_gen_text.setText(valor)

    def validarDatos(self):
        if len(self.valor_obj_gen) == 0:
            raise Exception("El objetivo general no puede estar vacío")
        
    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def closeEvent(self, event):
        self.__presentador.desbloquearVentanaSelec()
        event.accept()