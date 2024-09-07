from Vista.AgActObj import AgActObj

class ActualizarObj(AgActObj):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Editar Objetivo")

        self.aceptar_btn.clicked.connect(self.__presentador.actualizarObj)