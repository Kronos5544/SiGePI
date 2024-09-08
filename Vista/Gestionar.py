from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

class Gestionar(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/Gestionar.ui", self)

        self.tabla.itemClicked.connect(self.activarBtnEdicion)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def activarBtnEdicion(self):
        self.editar_btn.setEnabled(True)
        self.eliminar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.editar_btn.setEnabled(False)
        self.eliminar_btn.setEnabled(False)

    def vaciarTabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

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

    def configurarTabla(self, elementos):
        self.tabla.setColumnCount(len(elementos))
        self.tabla.setHorizontalHeaderLabels(elementos)
        self.tabla.resizeColumnsToContents()

    