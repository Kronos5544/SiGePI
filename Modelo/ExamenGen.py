from Modelo.Examen import Examen

class ExamenGen(Examen): 
    def __init__(self, fecha, asignatura, calificado):
        super().__init__(fecha, asignatura)
        self.__calificado = calificado
    
    @property
    def calificado(self):
        return self.__calificado
    @calificado.setter
    def calificado(self, value):
        self.__calificado = value