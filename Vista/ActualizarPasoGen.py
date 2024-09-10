from Vista.AgActPasoGen import AgActPasoGen

class ActualizarPasoGen(AgActPasoGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Editar Paso Gen")

        self.aceptar_btn.clicked.connect(self.__presentador.editarPasoGen)

    def desactivar_asignatura_selec(self):
        self.__asignatura_selec.setEnabled(False)
    
    def activar_asignatura_selec(self):
        self.__asignatura_selec.setEnabled(True)