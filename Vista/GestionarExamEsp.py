from Vista.Gestionar import Gestionar

class GestionarExamEsp(Gestionar):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Administrar Calificaciones")

        self.agregar_btn.clicked.connect(self.__presentador.selecVentana)
        self.editar_btn.clicked.connect(self.__presentador.editarVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarExamenEsp)
        
    def desactivarBtnAgregar(self):
        self.agregar_btn.setEnabled(False)

    def activarBtnAgregar(self):
        self.agregar_btn.setEnabled(True)

    def activarBtnEdicion(self):
        if self.__presentador.permitirEdicion():
            self.editar_btn.setEnabled(True)
            self.eliminar_btn.setEnabled(True)

    def desactivarBtnEdicion(self):
        if self.__presentador.permitirEdicion():
            self.editar_btn.setEnabled(False)
            self.eliminar_btn.setEnabled(False)
        else:
            self.editar_btn.setEnabled(False)
            self.eliminar_btn.setEnabled(False)
            self.desactivarBtnAgregar()