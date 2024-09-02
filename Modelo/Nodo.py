class Nodo:
    def __init__(self, elemento):
        self.__elemento = elemento
        self.__siguiente = None

    def obtener_elemento(self):
        return self.__elemento

    def obtener_siguiente(self):
        return self.__siguiente

    def cambiar_elemento(self, elemento):
        self.__elemento = elemento

    def cambiar_siguiente(self, siguiente):
        self.__siguiente = siguiente