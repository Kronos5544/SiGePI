from Vista.GestionarPasoGen import GestionarPasoGen
from Vista.AgregarPasoGen import AgregarPasoGen
from Vista.Seleccion import Seleccion
from Vista.ActualizarPasoGen import ActualizarPasoGen
from Modelo.PasoGen import PasoGen
from Presentador.PresentadorObj import PresentadorObj
from collections import deque
from copy import copy

class PresentadorPasoGen:
    def __init__(self, rep, vista_princ, preg):
        self.__rep = rep
        self.__vista_princ = vista_princ
        self.__preg = preg

    @property
    def max_cal_preg(self):
        return self.__preg.max_cal

    def iniciar(self):
        self.__vista = GestionarPasoGen(self)
        self.conf_var()
        self.conf_cola_var()
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def cargarDatos(self):
        self.__pasos = self.__rep.obtenerPasoGen(self.__preg, self.__vista.valor_variante)
        self.__vista.desactivarBtnEdicion()
        tabla = self.__rep.unirPasoGenObj(self.__preg, self.__vista.valor_variante)
        self.__vista.valor_cal_actual = self.__rep.calcCalPreg(self.__preg, self.__vista.valor_variante)
        self.__vista.vaciarTabla()
        for e in tabla:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, str(e.obtener_elemento()[0]))
            self.__vista.agregar_elemento_tabla(i, 1, str(e.obtener_elemento()[1]))
            self.__vista.agregar_elemento_tabla(i, 2, str(e.obtener_elemento()[2]))
            self.__vista.agregar_elemento_tabla(i, 3, str(e.obtener_elemento()[3]))
        self.__vista.tabla.resizeColumnsToContents()

        if not self.permitirEdicion(): 
            self.__vista.desactivarBtnEliminarVar()
            self.__vista.desactivarBtnAgregar()
        else:
            self.__vista.activarBtnEliminarVar()
            self.__vista.activarBtnAgregar()
            
        if self.__vista.valor_variante == "A":
            self.__vista.desactivarBtnEliminarVar()
        
        self.__var_anterior = self.__vista.valor_variante
            
    def permitirEdicion(self):
        var = self.__vista.variante_selec.itemText(self.__variantes.index(self.__vista.valor_variante) + 1)
        if var == "Añadir":
            return True
        else:
            return False

    def conf_var(self):
        self.__variantes = self.__rep.variantePreg(self.__preg)
        variantes = copy(self.__variantes)
        variantes.append("Añadir")
        self.__vista.valor_variante = variantes

    def conf_cola_var(self):
        alfabeto = [letra for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.__cola = deque(alfabeto)
        for i in range(len(self.__rep.variantePreg(self.__preg))):
            self.__cola.popleft()

    def agregarVariante(self):
        try:
            if self.__rep.compVariante(self.__preg, self.__var_anterior) == "OK":
                selec = self.__vista.mostrarAdvertencia("Después de añadir una nueva variante no podrá editar la variante anterior a no ser que elimine la nueva variante\n¿Está seguro que desea continuar?")
                if selec:
                    self.__variantes.append(self.__cola.popleft())
                    variantes = copy(self.__variantes)
                    variantes.append("Añadir")
                    self.__vista.desactivarCambVar()
                    self.__vista.valor_variante = variantes
                    self.__vista.variante_selec.setCurrentText(self.__variantes[-1])
                    self.__vista.activarCambVar()
            else:
                self.__vista.variante_selec.setCurrentText(self.__var_anterior)
                raise Exception("Para poder añadir nuevas variantes debe primero la suma de las calificaciones máximas de los pasos coincidir con la calificación máxima de la pregunta asociada")
        except Exception as error:
            self.__vista.mostrarError(str(error))

    def eliminarVariante(self):
        try:
            selec = self.__vista.mostrarAdvertencia("Eliminará todos los pasos asociados a esta variante\n¿Seguro de que desea continuar?")
            if selec:
                for e in self.__pasos:
                    self.__rep.eliminarPasoGen(e.obtener_elemento())
                self.__variantes.pop()
                variantes = copy(self.__variantes)
                variantes.append("Añadir")
                self.__vista.desactivarCambVar()
                self.__vista.valor_variante = variantes
                self.__vista.variante_selec.setCurrentText(self.__variantes[-1])
                self.conf_cola_var()
                self.__vista.activarCambVar()
        except Exception() as error:
            self.__vista.mostrarError(str(error))

    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def eliminarPasoGen(self):
        try:
            selec = self.__vista.mostrarAdvertencia("Eliminará el último Paso\n¿Seguro que desea continuar?")
            if selec:
                self.__paso_anterior = self.__pasos.nodo_en(len(self.__pasos) - 1).obtener_elemento()
                self.__rep.eliminarPasoGen(self.__paso_anterior)
                self.cargarDatos()
        except Exception as error:
            self.__vista.mostrarError(str(error))

#---------------Ventana Añadir paso General--------------------
    def agregarPasoGenVentana(self):
        self.__ag_act = AgregarPasoGen(self)
        self.__ag_act.show()
        self.__vista.bloquearVentana()

    def agregarPasoGen(self):
        try:
            self.__ag_act.validarDatos()
            paso = PasoGen(len(self.__pasos) + 1, self.__vista.valor_variante, self.__preg.no_pregunta, self.__preg.fecha, self.__ag_act.valor_max_cal, int(self.__ag_act.valor_id_obj))
            self.__rep.insertarPasoGen(paso)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))

#----------------Ventana Seleccionar-----------------
    def selecVentana(self):
        self.__selec = Seleccion(self)
        self.cargarDatosSelec()
        self.__selec.show()
        self.__ag_act.bloquearVentana()
        
    def cargarDatosSelec(self):
        self.__selec.desactivarBtnSelec()
        self.__selec.vaciarTabla()
        self.__selec.configurarNombreVentana("Seleccionar Objetivo")
        self.__selec.configurarTabla(["ID Objetivo", "Objetivo Especifico", "Objetivo General"])
        self.__selec.confNombAbrirGestorBtn("Gestor Objetivos")
        objetivos = self.__rep.obtenerObjXAsig(self.__rep.obtenerAsigExam(self.__preg.fecha))
        for objetivo in objetivos:
            i = self.__selec.tabla.rowCount()
            self.__selec.tabla.insertRow(i)
            self.__selec.agregar_elemento_tabla(i, 0, str(objetivo.obtener_elemento().id_obj))
            self.__selec.agregar_elemento_tabla(i, 1, objetivo.obtener_elemento().desc_obj_esp)
            self.__selec.agregar_elemento_tabla(i, 2, objetivo.obtener_elemento().desc_obj_gen)
            self.__selec.agregar_elemento_tabla(i, 3, objetivo.obtener_elemento().asignatura)
        self.__selec.tabla.resizeColumnsToContents()

    def selec(self):
        fila_selec = self.__selec.tabla.currentRow()
        self.__ag_act.valor_id_obj = self.__selec.tabla.item(fila_selec, 0).text()
        self.__selec.close()

    def gestor(self):
        self.__gestor_obj = PresentadorObj(self.__rep, self.__ag_act)
        self.__selec.close()
        self.__gestor_obj.iniciar()
        self.__ag_act.bloquearVentana()

    def desbVentanaAnterior(self):
        self.__ag_act.desbloquearVentana()

#-------------Ventana Editar Paso------------------
    def editarPasoGenVentana(self):
        self.__ag_act = ActualizarPasoGen(self)
        fila_selec = self.__vista.tabla.currentRow()
        self.__paso_anterior = self.__pasos.nodo_en(fila_selec).obtener_elemento()
        self.__ag_act.valor_max_cal = self.__paso_anterior.max_cal
        self.__ag_act.valor_id_obj = self.__paso_anterior.id_obj
        self.__ag_act.show()
        self.__vista.bloquearVentana()

    def editarPasoGen(self):
        try:
            self.__ag_act.validarDatos()
            nuevo_paso = PasoGen(self.__paso_anterior.no_paso, self.__paso_anterior.variante, self.__paso_anterior.no_pregunta, self.__paso_anterior.fecha, self.__ag_act.valor_max_cal, str(self.__ag_act.valor_id_obj))
            self.__rep.actualizarPasoGen(self.__paso_anterior, nuevo_paso)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))


    