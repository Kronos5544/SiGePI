from Modelo.ObjGen import ObjGen

class ObjEsp(ObjGen):
    def __init__(self, id_obj, tipo, asignatura, desc, id_obj_gen):
        super().__init__(id_obj, tipo, asignatura, desc)
        self.__id_obj_gen = id_obj_gen

    @property
    def id_obj_gen(self):
        return self.__id_obj_gen
    @id_obj_gen.setter
    def id_obj_gen(self, valor):
        self.__id_obj_gen = valor