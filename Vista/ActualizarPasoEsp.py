from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

class ActualizarPasoEsp(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/ActualizarPasoEsp.ui", self)

        self.configurarTabla(["No Paso", "Calificación", "Máx Calificación", "Objetivo Esp", "Objetivo General"])
        self.tabla.itemClicked.connect(self.__presentador.rellenarCalXTabla)
        self.label.setText("Calificación:")

        self.aceptar_btn.clicked.connect(self.__presentador.editarCalPaso)
        self.cerrar_btn.clicked.connect(self.close)

    @property
    def valor_variante(self):
        return self.variante_selec.currentText()
    @valor_variante.setter
    def valor_variante(self, variantes):
        self.variante_selec.clear()
        self.variante_selec.addItems(variantes)

    @property
    def valor_cal(self):
        return self.cal_num.value()
    @valor_cal.setter
    def valor_cal(self, value):
        self.cal_num.setValue(value)

    def activarBtnEdicion(self):
        self.aceptar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.aceptar_btn.setEnabled(False)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.__presentador.cargarDatos()
        self.setEnabled(True) 

    def configurarTabla(self, elementos):
        self.tabla.setColumnCount(len(elementos))
        self.tabla.setHorizontalHeaderLabels(elementos)
        self.tabla.resizeColumnsToContents()
 
    def desactivarCambVar(self):
        self.variante_selec.currentIndexChanged.connect(self.funcAux)

    def activarCambVar(self):
        self.variante_selec.currentIndexChanged.connect(self.__presentador.cambVar)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error) 

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
            
    def vaciarTabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

    def restablecerDatos(self):
        self.valor_cal = 0

    def closeEvent(self, event):
        self.__presentador.desbloquearVentPrinc()
        event.accept()

    def funcAux(self):
        pass