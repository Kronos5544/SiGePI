from Modelo.Pregunta import Pregunta
from Modelo.ExamenEspPadre import ExamenEspPadre

class PreguntaEsp(Pregunta, ExamenEspPadre):
    def __init__(self, fecha, id_est, no_pregunta, calificacion):
        Pregunta.__init__(self, no_pregunta)
        ExamenEspPadre.__init__(self, id_est, fecha)
        self.__calificacion = calificacion
    
    @property
    def calificacion(self):
        return self.__calificacion
    @calificacion.setter
    def calificacion(self, valor):
        self.__calificacion = valor