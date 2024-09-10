from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

class GestionarPasoGen(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/GestionarPasoGen.ui", self)

        self.tabla.itemClicked.connect(self.activarBtnEdicion)
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["No Paso", "Máx Calificación", "Objetivo Esp", "Objetivo Gen"])
        self.tabla.resizeColumnsToContents()
        self.variante_selec.currentIndexChanged.connect(self.cambiarVar)

        self.agregar_btn.clicked.connect(self.__presentador.agregarPasoGenVentana)
        self.editar_btn.clicked.connect(self.__presentador.editarPasoGenVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarPasoGen)
        self.eliminar_var_btn.clicked.connect(self.__presentador.eliminarVariante)
        self.cerrar_btn.clicked.connect(self.close)
        self.cal_act.setText("Calificación Total: 0/0")

    @property
    def valor_cal_actual(self):
        valor = float(self.cal_act.text().split(": ")[1].split("/")[0])
        return valor
    @valor_cal_actual.setter
    def valor_cal_actual(self, valor_act):
        self.cal_act.setText(f"Calificación Total: {valor_act}/{self.__presentador.max_cal_preg}")

    @property
    def valor_variante(self):
        return self.variante_selec.currentText()
    @valor_variante.setter
    def valor_variante(self, variantes):
        self.variante_selec.clear()
        self.variante_selec.addItems(variantes)        

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def activarBtnEdicion(self):
        if self.__presentador.permitirEdicion:
            self.editar_btn.setEnabled(True)
            self.eliminar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.editar_btn.setEnabled(False)
        self.eliminar_btn.setEnabled(False)

    def desactivarBtnEliminarVar(self):
        self.eliminar_var_btn.setEnabled(False)

    def activarBtnEliminarVar(self):
        self.eliminar_var_btn.setEnabled(True)

    def desactivarBtnAgregar(self):
        self.agregar_btn.setEnabled(False)

    def activarBtnAgregar(self):
        self.agregar_btn.setEnabled(True)

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
    
    def cambiarVar(self):
        if self.valor_variante == "Añadir":
            self.__presentador.agregarVariante()
        elif self.valor_variante != "":
            self.__presentador.cargarDatos()

    def desactivarCambVar(self):
        self.variante_selec.currentIndexChanged.connect(self.funcAux)

    def activarCambVar(self):
        self.variante_selec.currentIndexChanged.connect(self.cambiarVar)

    def funcAux(self):
        pass