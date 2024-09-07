from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

class GestionarObj(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/GestionarObj.ui", self)
        
        self.agregar_btn.clicked.connect(self.__presentador.agregarObjVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarObj)
        self.editar_btn.clicked.connect(self.__presentador.actualizarObjVentana)

        self.tabla_obj.setColumnCount(3)
        self.tabla_obj.setHorizontalHeaderLabels(["Objetivo Específico", "Objetivo General", "Asignatura"])
        self.tabla_obj.resizeColumnsToContents()
        self.tabla_obj.itemClicked.connect(self.activarBtnEdicion)

    def vaciar_tabla(self):
        e = self.tabla_obj.rowCount()
        for i in range(e):
            self.tabla_obj.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla_obj.setItem(fila, columna, QTableWidgetItem(elemento))
    
    def activarBtnEdicion(self):
        self.editar_btn.setEnabled(True)
        self.eliminar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.editar_btn.setEnabled(False)
        self.eliminar_btn.setEnabled(False)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)

    def closeEvent(self, event):
        if self.isEnabled():
            self.__presentador.desbloquearVentPrinc()
            event.accept()
        else:
            event.ignore()


    
