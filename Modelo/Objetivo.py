class Objetivo:
    def __init__(self, id_obj, asignatura, desc_obj_esp, desc_obj_gen):
        self.__id_obj = id_obj
        self.__asignatura = asignatura
        self.__desc_obj_esp = desc_obj_esp
        self.__desc_obj_gen = desc_obj_gen

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
    def desc_obj_esp(self):
        return self.__desc_obj_esp
    @desc_obj_esp.setter
    def desc_obj_esp(self, valor):
        self.__desc_obj_esp = valor

    @property
    def desc_obj_gen(self):
        return self.__desc_obj_gen
    @desc_obj_gen.setter
    def desc_obj_gen(self, valor):
        self.__desc_obj_gen = valor