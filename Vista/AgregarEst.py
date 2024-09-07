from Vista.AgActEst import AgActEst

class AgregarEst(AgActEst):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Añadir Estudiante")

        self.aceptar_btn.clicked.connect(self.__presentador.agregarEst)