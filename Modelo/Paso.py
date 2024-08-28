from Modelo.Pregunta import Pregunta

class Paso(Pregunta):
    def __init__(self, no_pregunta, no_paso, variante):
        super().__init__(no_pregunta)
        self.__no_paso = no_paso
        self.__variante = variante

    @property
    def no_paso(self):
        return self.__no_paso
    @no_paso.setter
    def no_paso(self, valor):
        self.__no_paso = valor

    @property
    def variante(self):
        return self.__variante
    @variante.setter
    def variante(self, valor):
        self.__variante = valor