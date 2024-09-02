from Modelo.ExamenEspPadre import ExamenEspPadre
from Modelo.Paso import Paso

class PasoEsp(Paso, ExamenEspPadre):
    def __init__(self, no_pregunta, no_paso, variante, id_est, fecha, asignatura, calificacion):
        Paso.__init__(self, no_pregunta, no_paso, variante)
        ExamenEspPadre.__init__(self, id_est, fecha, asignatura)
        self.__calificacion = calificacion

    @property
    def calificacion(self):
        return self.__calificacion
    @calificacion.setter
    def calificacion(self, valor):
        self.__calificacion = valor