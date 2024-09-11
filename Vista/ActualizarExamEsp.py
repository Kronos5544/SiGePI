from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

class ActualizarExamEsp(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/ActualizarExamEsp.ui", self)

        self.configurarTabla(["No Pregunta", "Calificación", "Máx Calificación"])
        self.tabla.itemClicked.connect(self.activarBtnEdicion)

        self.aceptar_btn.clicked.connect(self.__presentador.editarDescOrt)
        self.editar_btn.clicked.connect(self.__presentador.editarCalPregVentana)
        self.cerrar_btn.clicked.connect(self.close)

    @property
    def valor_est_id(self):
        return self.est_id_text.text()
    @valor_est_id.setter
    def valor_est_id(self, value):
        self.est_id_text.setText(value)

    @property
    def valor_desc_ort(self):
        return self.desc_num.value()
    @valor_desc_ort.setter
    def valor_desc_ort(self, value):
        self.desc_num.setValue(value)

    def activarBtnEdicion(self):
        self.editar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        self.editar_btn.setEnabled(False)

    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.__presentador.cargarDatos()
        self.setEnabled(True) 

    def configurarTabla(self, elementos):
        self.tabla.setColumnCount(len(elementos))
        self.tabla.setHorizontalHeaderLabels(elementos)
        self.tabla.resizeColumnsToContents()
    
    def vaciarTabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)
 

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error) 

    def closeEvent(self, event):
        self.__presentador.desbloquearVentPrinc()
        event.accept()