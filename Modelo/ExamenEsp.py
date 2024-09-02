from Modelo.ExamenEspPadre import ExamenEspPadre

class ExamenEsp(ExamenEspPadre):
    def __init__(self, id_est, fecha, calificacion, desc_ort):
        super().__init__(id_est, fecha)
        self.__calificacion = calificacion
        self.__desc_ort = desc_ort

    @property
    def calificacion(self):
        return self.__calificacion
    @calificacion.setter
    def calificacion(self, valor):
        self.__calificacion = valor

    @property
    def desc_ort(self):
        return self.__desc_ort
    @desc_ort.setter
    def desc_ort(self, valor):
        self.__desc_ort = valor