from Vista.Gestionar import Gestionar

class GestionarEst(Gestionar):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.configurarTabla(["Id"])
