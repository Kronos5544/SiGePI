from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

class Seleccion(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/Seleccion.ui", self)

        self.tabla.itemDoubleClicked.connect(self.__presentador.selec)
        self.tabla.itemClicked.connect(self.activarBtnSelec)
        self.selec_btn.clicked.connect(self.__presentador.selec)
        self.abrir_gestor_btn.clicked.connect(self.__presentador.gestor)
        self.cancelar_btn.clicked.connect(self.close)

    def configurarTabla(self, elementos):
        self.tabla.setColumnCount(len(elementos))
        self.tabla.setHorizontalHeaderLabels(elementos)
        self.tabla.resizeColumnsToContents()

    def desactivarBtnSelec(self):
        self.selec_btn.setEnabled(False)

    def activarBtnSelec(self):
        self.selec_btn.setEnabled(True)

    def configurarNombreVentana(self, nombre):
        self.setWindowTitle(nombre)

    def confNombAbrirGestorBtn(self, nombre):
        self.abrir_gestor_btn.setText(nombre)

    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def vaciarTabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)

    def closeEvent(self, event):
        self.__presentador.desbVentanaAnterior()
