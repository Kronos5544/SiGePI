from Vista.AgActPregGen import AgActPregGen

class ActualizarPregGen(AgActPregGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Editar Pregunta")

        self.aceptar_btn.clicked.connect(self.__presentador.actualizarPregGen)
        