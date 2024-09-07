from Vista.AgActEst import AgActEst

class ActualizarEst(AgActEst):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Actualizar Estudiante")

        self.aceptar_btn.clicked.connect(self.__presentador.actualizarEst)