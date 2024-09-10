from Vista.AgActExamGen import AgActExamGen

class AgregarExamGen(AgActExamGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Agregar Examen")
        self.ocultarClaveBtn(True)

        self.aceptar_btn.clicked.connect(self.__presentador.agregarExam)

    