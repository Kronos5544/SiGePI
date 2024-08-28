class ObjGen:
    def __init__(self, id_obj, tipo, asignatura, desc):
        self.__id_obj = id_obj
        self.__tipo = tipo
        self.__asignatura = asignatura
        self.__desc = desc

    @property
    def id_obj(self):
        return self.__id_obj
    @id_obj.setter
    def id_obj(self, valor):
        self.__id_obj = valor

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def asignatura(self):
        return self.__asignatura
    @asignatura.setter
    def asignatura(self, valor):
        self.__asignatura = valor
    
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, valor):
        self.__desc = valor