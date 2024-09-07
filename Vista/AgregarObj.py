from Vista.AgActObj import AgActObj

class AgregarObj(AgActObj):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Añadir Objetivo")

        self.aceptar_btn.clicked.connect(self.__presentador.agregarObjetivo)
        

   