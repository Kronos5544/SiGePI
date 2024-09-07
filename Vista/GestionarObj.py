from Vista.Gestionar import Gestionar


class GestionarObj(Gestionar):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Gestionar Objetivos")
        
        self.agregar_btn.clicked.connect(self.__presentador.agregarObjVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarObj)
        self.editar_btn.clicked.connect(self.__presentador.actualizarObjVentana)

        self.configurarTabla(["Objetivo Específico", "Objetivo General", "Asignatura"])
        self.tabla_obj = self.tabla
        

    
    
    

    


    
