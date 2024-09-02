class Examen:
    def __init__(self, fecha):
        self.__fecha = fecha

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, value):
        self.__fecha = value

