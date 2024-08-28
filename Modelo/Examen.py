class Examen:
    def __init__(self, fecha, asignatura):
        self.__fecha = fecha
        self.__asignatura = asignatura

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, value):
        self.__fecha = value

    @property
    def asignatura(self):
        return self.__asignatura
    @asignatura.setter
    def asignatura(self, value):
        self.__asignatura = value

