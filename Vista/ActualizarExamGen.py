from Vista.AgActExamGen import AgActExamGen

class ActualizarExamGen(AgActExamGen):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Actualizar Examen")
        self.ocultarClaveBtn(False)

        self.aceptar_btn.clicked.connect(self.__presentador.actualizarExam)

    def desactivar_asignatura_selec(self):
        self.asignatura_selec.setEnabled(False)
    
    def activar_asignatura_selec(self):
        self.asignatura_selec.setEnabled(True)