from Modelo.Pregunta import Pregunta
from Modelo.Examen import Examen

class PreguntaGen(Pregunta, Examen):
    def __init__(self, fecha, no_pregunta, max_cal):
        Pregunta.__init__(self, no_pregunta)
        Examen.__init__(self, fecha)
        self.__max_cal = max_cal

    @property
    def max_cal(self):
        return self.__max_cal
    @max_cal.setter
    def max_cal(self, valor):
        self.__max_cal = valor