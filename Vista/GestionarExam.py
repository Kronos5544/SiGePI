from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

class GestionarExam(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('./Vista/ui/GestionarExam.ui', self)
        self.tabla.itemClicked.connect(self.activarBtnEdicion)

        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Fecha (aaaa/mm/dd)", "Asignatura", "Calificado"])
        self.tabla.resizeColumnsToContents()

        self.agregar_btn.clicked.connect(self.__presentador.agregarExamVentana)
        self.editar_btn.clicked.connect(self.__presentador.actualizarExamVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarExam)
        self.finalizar_btn.clicked.connect(self.__presentador.finalizarCalExam)


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

    def mostrarAdvertencia(self, mensaje):
            # Crear la ventana de alerta
            advertencia = QMessageBox(self)
            advertencia.setWindowTitle("Advertencia")
            advertencia.setIcon(QMessageBox.Warning)
            advertencia.setText(mensaje)
            
            # Añadir botones personalizados
            boton_aceptar = advertencia.addButton("Aceptar", QMessageBox.AcceptRole)
            boton_cancelar = advertencia.addButton("Cancelar", QMessageBox.RejectRole)
            advertencia.setDefaultButton(boton_aceptar) # Establecer Aceptar como botón predeterminado

            # Mostrar la ventana de alerta
            advertencia.exec_()

            # Evaluar la respuesta
            if advertencia.clickedButton() == boton_aceptar:
                return True
            else:
                return False
        
    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error)

    def closeEvent(self, event):
        if self.isEnabled():
            self.__presentador.desbloquearVentPrinc()
            event.accept()
        else:
            event.ignore()
