from Modelo.Paso import Paso
from Modelo.Examen import Examen

class PasoGen(Paso, Examen):
    def __init__(self, no_pregunta, no_paso, variante, fecha, asignatura, max_cal):
        Paso.__init__(self, no_pregunta, no_paso, variante)
        Examen.__init__(self, fecha, asignatura)
        self.__max_cal = max_cal

    @property
    def max_cal(self):
        return self.__max_cal
    @max_cal.setter
    def max_cal(self, valor):
        self.__max_cal = valor 


