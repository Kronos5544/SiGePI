from Modelo.Paso import Paso
from Modelo.Examen import Examen

class PasoGen(Paso, Examen):
    def __init__(self, no_paso, variante, no_pregunta, fecha, max_cal, id_obj):
        Paso.__init__(self, no_pregunta, no_paso, variante)
        Examen.__init__(self, fecha)
        self.__max_cal = max_cal
        self.__id_obj = id_obj

    @property
    def max_cal(self):
        return self.__max_cal
    @max_cal.setter
    def max_cal(self, valor):
        self.__max_cal = valor 

    @property
    def id_obj(self):
        return self.__id_obj
    @id_obj.setter
    def id_obj(self, valor):
        self.__id_obj = valor


