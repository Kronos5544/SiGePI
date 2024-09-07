from Vista.GestionarEst import GestionarEst

class PresentadorEst:
    def __init__(self, rep, vista_princ):
        self.__rep = rep
        self.__vista_princ = vista_princ

    def iniciar(self):
        self.__vista = GestionarEst(self)
        self.__vista.show()
        