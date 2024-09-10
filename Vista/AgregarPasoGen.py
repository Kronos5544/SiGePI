from Vista.AgActPasoGen import AgActPasoGen

class AgregarPasoGen(AgActPasoGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Añadir Paso Gen")

        self.aceptar_btn.clicked.connect(self.__presentador.agregarPasoGen)