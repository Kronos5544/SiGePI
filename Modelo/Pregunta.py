class Pregunta:
    def __init__(self, no_pregunta):
        self.__no_pregunta = no_pregunta

    @property
    def no_pregunta(self):
        return self.__no_pregunta
    @no_pregunta.setter
    def no_pregunta(self, valor):
        self.__no_pregunta = valor
        
