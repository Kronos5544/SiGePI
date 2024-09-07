class EstudiantePadre():
    def __init__(self, est_id):
        self.__est_id = est_id

    @property
    def est_id(self):
        return self.__est_id
    @est_id.setter
    def est_id(self, valor):
        self.__est_id = valor
        