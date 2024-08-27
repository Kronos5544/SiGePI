from Vista.GestionarExam import GestionarExam

class PresentadorExam:
    def __init__(self):
        pass

    def iniciar(self):
        self.__vista = GestionarExam(self)
        self.__vista.show()
        
