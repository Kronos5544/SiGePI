from Vista.GestionarObj import GestionarObj
from Vista.AgregarObj import AgregarObj
from Vista.Seleccion import Seleccion
from Vista.NuevoObjetivoGen import NuevoObjetivoGen
from Vista.ActualizarObj import ActualizarObj
from Modelo.ListaEnlazada import ListaEnlazada
from Modelo.Objetivo import Objetivo

class PresentadorObj:
    def __init__(self, rep, vista_princ):
        self.__rep = rep
        self.__vista_princ = vista_princ
        self.__obj = ListaEnlazada()

#------------------Ventana Gestionar Objetivo----------------------------------------
    def iniciar(self):
        self.__vista = GestionarObj(self)
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def cargarDatos(self):
        self.__vista.desactivarBtnEdicion()
        self.__obj = self.__rep.obtenerObj()
        self.__vista.vaciarTabla()
        for objetivo in self.__obj:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, objetivo.obtener_elemento().desc_obj_esp)
            self.__vista.agregar_elemento_tabla(i, 1, objetivo.obtener_elemento().desc_obj_gen)
            self.__vista.agregar_elemento_tabla(i, 2, objetivo.obtener_elemento().asignatura)
        self.__vista.tabla.resizeColumnsToContents()

    def eliminarObj(self):
        fila_selec = self.__vista.tabla.currentRow()
        if fila_selec != -1:
            self.__rep.eliminarObj(self.__obj.nodo_en(fila_selec).obtener_elemento())
            self.cargarDatos()

#---------------------Ventana Agregar/Actualizar Objetivos--------------------------------
    
    def agregarObjVentana(self):
        self.__ag_act = AgregarObj(self)
        self.__vista.bloquearVentana()
        self.__ag_act.show()

    def agregarObjetivo(self):
        try:
            self.__ag_act.validarDatos()
            objetivo = Objetivo(1, self.__ag_act.valor_asignatura, self.__ag_act.valor_obj_esp, self.__ag_act.valor_obj_gen)
            self.__rep.insertarObj(objetivo)
            self.__ag_act.restablecerValores()
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))

#-------------------Ventana Seleccionar Objetivo General------------------------------------
    def seleccionarVentana(self):
        self.__selec = Seleccion(self)
        self.cargarDatosObjGen()
        self.__selec.configurarNombreVentana("Selección Objetivo")
        self.__selec.confNombAbrirGestorBtn("Nuevo")
        self.__selec.show()
        self.__ag_act.bloquearVentana()
    
    def desbloquearVentanaSelec(self):
        self.__selec.desbloquearVentana()

    def desbVentanaAnterior(self):
        self.__ag_act.desbloquearVentana()

    def cargarDatosObjGen(self):
        self.__selec.vaciarTabla()
        self.__selec.configurarTabla(["Objetivo General"])
        lista = self.__rep.objetivoGenXAsig(self.__ag_act.valor_asignatura)
        for objetivo_gen in lista:
            i = self.__selec.tabla.rowCount()
            self.__selec.tabla.insertRow(i)
            self.__selec.agregar_elemento_tabla(i, 0, objetivo_gen.obtener_elemento())
        self.__selec.tabla.resizeColumnsToContents()

    def selec(self):
        try:
            fila_select = self.__selec.tabla.currentRow() #currentRow() devuelve el elemento de la fila que está siendo seleccionado, si no hay nunguno seleccionado devuelve -1
            if fila_select != -1: 
                self.__ag_act.valor_obj_gen = self.__selec.tabla.item(fila_select, 0).text()
                self.__selec.close()
            else:
                raise Exception("Necesita seleccionar un objetivo general de la tabla")
        except Exception as error:
            self.__selec.mostrarError(str(error))


#---------------------Ventana Nuevo Objetivo General--------------------------------------
    def gestor(self):
        self.__nuevo_obj_gen = NuevoObjetivoGen(self)
        self.__selec.bloquearVentana()
        self.__nuevo_obj_gen.show()
    
    def agregarNuevoObjGen(self):
        try:
            self.__nuevo_obj_gen.validarDatos()
            if self.__nuevo_obj_gen.valor_obj_gen in (list(map(lambda x: x.obtener_elemento(), self.__rep.objetivoGenXAsig(self.__ag_act.valor_asignatura)))):
                raise Exception("El objetivo general ya existe")
            self.__ag_act.valor_obj_gen = self.__nuevo_obj_gen.valor_obj_gen
            self.__nuevo_obj_gen.close()
            self.__selec.close()
        except Exception as error:
            self.__nuevo_obj_gen.mostrarError(str(error))

#-----------------Ventana Actualizar Objetivo---------------------
    def actualizarObjVentana(self):
        self.__ag_act = ActualizarObj(self)
        fila_selec = self.__vista.tabla.currentRow()
        self.__obj_actualizar = self.__obj.nodo_en(fila_selec).obtener_elemento()
        self.cargarDatosActualizar()
        self.__vista.bloquearVentana()
        self.__ag_act.show()

    def actualizarObj(self):
        try:
            self.__ag_act.validarDatos()
            nuevo_obj = Objetivo(self.__obj_actualizar.id_obj, self.__ag_act.valor_asignatura, self.__ag_act.valor_obj_esp, self.__ag_act.valor_obj_gen)
            self.__rep.actualizarObj(nuevo_obj)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))


    def cargarDatosActualizar(self):
        self.__ag_act.valor_asignatura = self.__obj_actualizar.asignatura
        self.__ag_act.valor_obj_gen = self.__obj_actualizar.desc_obj_gen
        self.__ag_act.valor_obj_esp = self.__obj_actualizar.desc_obj_esp
        

        
    


        
        

        