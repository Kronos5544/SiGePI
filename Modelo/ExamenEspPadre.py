from Modelo.Examen import Examen

class ExamenEspPadre(Examen):
    def __init__(self, est_id, fecha):
        super().__init__(fecha)
        self.__est_id = est_id

    @property
    def est_id(self):
        return self.__est_id
    @est_id.setter
    def est_id(self, valor):
        self.__est_id = valor