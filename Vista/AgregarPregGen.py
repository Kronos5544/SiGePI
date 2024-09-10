from Vista.AgActPregGen import AgActPregGen

class AgregarPregGen(AgActPregGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Agregar Pregunta")
        
        self.aceptar_btn.clicked.connect(self.__presentador.agregarPregGen)