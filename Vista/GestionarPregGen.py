from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

class GestionarPregGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/GestionarPregGen.ui", self)

        self.tabla.itemClicked.connect(self.activarBtnEdicion)
        self.agregar_btn.clicked.connect(self.__presentador.agregarPregGenVentana)
        self.editar_preg_btn.clicked.connect(self.__presentador.actualizarPregGenVentana)
        self.editar_pasos_btn.clicked.connect(self.__presentador.pasosVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarPregGen)
        self.cerrar_btn.clicked.connect(self.close)

    @property
    def valor_cal_actual(self):
        return self.cal_act_text.text()
    @valor_cal_actual.setter
    def valor_cal_actual(self, valor):
        self.cal_act_text.setText(f"Calificación Total: {valor}/100.00")

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def activarBtnEdicion(self):
        self.editar_pasos_btn.setEnabled(True)
        self.editar_preg_btn.setEnabled(True)
        self.eliminar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.editar_pasos_btn.setEnabled(False)
        self.editar_preg_btn.setEnabled(False)
        self.eliminar_btn.setEnabled(False)

    def vaciarTabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)
        self.__presentador.cargarDatos()

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

    