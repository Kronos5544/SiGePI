from Modelo.Examen import Examen

class ExamenEspPadre(Examen):
    def __init__(self, id_est, fecha, asignatura):
        super().__init__(fecha, asignatura)
        self.__id_est = id_est

    @property
    def id_est(self):
        return self.__id_est
    @id_est.setter
    def id_est(self, valor):
        self.__id_est = valor