from Modelo.Examen import Examen

class ExamenGen(Examen): 
    def __init__(self, fecha, asignatura, calificado):
        super().__init__(fecha)
        self.__asignatura = asignatura
        self.__calificado = calificado
    
    @property
    def calificado(self):
        return self.__calificado
    @calificado.setter
    def calificado(self, value):
        self.__calificado = value

    @property
    def asignatura(self):
        return self.__asignatura
    @asignatura.setter
    def asignatura(self, value):
        self.__asignatura = value