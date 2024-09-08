from Vista.AgActExamGen import AgActExamGen

class AgregarExamGen(AgActExamGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.ocultarClaveBtn(True)