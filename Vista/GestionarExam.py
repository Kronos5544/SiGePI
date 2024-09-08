from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

class GestionarExam(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('./Vista/ui/GestionarExam.ui', self)
        self.tabla.itemClicked.connect(self.activarBtnEdicion)

        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Asignatura", "Calificado"])
        self.tabla.resizeColumnsToContents()

        self.agregar_btn.clicked.connect(self.__presentador.agregarExamVentana)


    def activarBtnEdicion(self):
        self.editar_btn.setEnabled(True)
        self.eliminar_btn.setEnabled(True)
        self.calificaciones_btn.setEnabled(True)
        self.finalizar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.editar_btn.setEnabled(False)
        self.eliminar_btn.setEnabled(False)
        self.calificaciones_btn.setEnabled(False)
        self.finalizar_btn.setEnabled(False)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))
    
    def vaciarTabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

    def closeEvent(self, event):
        if self.isEnabled():
            self.__presentador.desbloquearVentPrinc()
            event.accept()
        else:
            event.ignore()