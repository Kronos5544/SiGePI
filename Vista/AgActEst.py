from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox
from datetime import date

class AgActEst(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        self.__presentador = presentador
        uic.loadUi("./Vista/ui/AgActEst.ui", self)

        self.cancelar_btn.clicked.connect(self.close)

    @property
    def valor_ci(self):
        return self.ci_text.text().strip()
    @valor_ci.setter
    def valor_ci(self, valor):
        self.ci_text.setText(valor)

    def mostrarError(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def restablecerValores(self):
        self.valor_ci = ""
    
    def bloquearVentana(self):
        self.setEnabled(False)

    def desbloquearVentana(self):
        self.setEnabled(True)    

    def validarDatos(self):
        if len(self.valor_ci) == 0:
            raise Exception("El Carnet de Identidad no puede estar vacío")
        elif not self.valor_ci.isdigit():
            raise Exception("El Carnet de Identidad solo puede contener números")
        elif len(self.valor_ci) != 11:
            raise Exception("El Carnet de Identidad tiene que tener 11 números")
        self.validarCI(self.valor_ci)
    
    def validarCI(self, ci):
        try:
            hoy = date.today()
            annio = 1900 + int(ci[0:2]) #Le sumo a los primeros correspondientes al año en el ci 1900 para obtener un año válido sobre el que trabajar
            mes = int(ci[2:4])
            dia = int(ci[4:6])
            if (hoy.year - annio) > 100: #De esta forma calculo la diferencia entre el año actual y el año del ci
                annio += 100 #Esta función solo valida a carnet de personas menores de 100 años así que si la operación anterior da como resultado que la persona tiene más de 100 años se le suma 100 al año para así pasar al sigo 21
            date(annio, mes, dia) #Comprueba que la fecha del ci es una fecha válida, de no serlo devuelve un error
        except Exception:
            raise Exception("El Carnet de identidad es inválido")

    def closeEvent(self, event):
        self.__presentador.desbloquearVentana()
        self.__presentador.cargarDatos()
        event.accept()