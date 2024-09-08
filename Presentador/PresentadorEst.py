from Vista.GestionarEst import GestionarEst
from Vista.AgregarEst import AgregarEst
from Vista.ActualizarEst import ActualizarEst
from Modelo.Estudiante import Estudiante

class PresentadorEst:
    def __init__(self, rep, vista_princ):
        self.__rep = rep
        self.__vista_princ = vista_princ

#------------Vista GestionarEst-------------------------------------
    def iniciar(self):
        self.__vista = GestionarEst(self)
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def cargarDatos(self):
        self.__vista.desactivarBtnEdicion()
        self.__est = self.__rep.obtenerEstudiante()
        self.__vista.vaciarTabla()
        for estudiante in self.__est:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, estudiante.obtener_elemento().est_id)
        self.__vista.tabla.resizeColumnsToContents()

    def eliminarEst(self):
        fila_selec = self.__vista.tabla.currentRow()
        if fila_selec != -1:
            selec = self.__vista.mostrarAdvertencia("Se eliminarán todos los exámenes asociados a este estudiante\n¿Desea continuar?")
            if selec:
                self.__rep.eliminarEstudiante(self.__est.nodo_en(fila_selec).obtener_elemento())
                self.cargarDatos()

    
#---------------Vista Ventana Agregar/Actualizar Estudiantes----------------------------
    def agregarEstVentana(self):
        self.__ag_act_est = AgregarEst(self)
        self.__ag_act_est.show()
        self.__vista.bloquearVentana()

    def agregarEst(self):
        try:
            self.__ag_act_est.validarDatos()
            est = Estudiante(self.__ag_act_est.valor_ci)
            self.__rep.insertarEstudiante(est)
            self.__ag_act_est.restablecerValores()
            self.__ag_act_est.close()
        except Exception as error:
            self.__ag_act_est.mostrarError(str(error))

    def actualizarEstVentana(self):
        self.__ag_act_est = ActualizarEst(self)
        self.__ag_act_est.restablecerValores()
        fila_selec = self.__vista.tabla.currentRow()
        self.__anterior_est = self.__est.nodo_en(fila_selec).obtener_elemento()
        self.__ag_act_est.valor_ci = self.__anterior_est.est_id
        self.__ag_act_est.show()
        self.__vista.bloquearVentana()

    def actualizarEst(self):
        try:
            self.__ag_act_est.validarDatos()
            nuevo_est = Estudiante(self.__ag_act_est.valor_ci)
            self.__rep.actualizarEstudiante(self.__anterior_est, nuevo_est)
            self.__ag_act_est.restablecerValores()
            self.__ag_act_est.close()
        except Exception as error:
            self.__ag_act_est.mostrarError(str(error))

            

    
        
        