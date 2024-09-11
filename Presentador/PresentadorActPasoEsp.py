from Vista.ActualizarPasoEsp import ActualizarPasoEsp
from Modelo.PreguntaGen import PreguntaGen
from Modelo.PasoEsp import PasoEsp

class PresentadorActPasoEsp:
    def __init__(self, rep, vista_princ, preg_esp):
        self.__rep = rep
        self.__vista_princ = vista_princ
        self.__preg_esp = preg_esp

    def iniciar(self):
        self.__vista = ActualizarPasoEsp(self)
        self.conf_var()
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def cargarDatos(self):
        self.__pasos = self.__rep.obtenerPasoEsp(self.__preg_esp, self.__vista.valor_variante)
        pasos = self.__rep.unirPasoEspGenObj(self.__preg_esp, self.__vista.valor_variante)
        self.__vista.vaciarTabla()
        self.__vista.restablecerDatos()
        self.__vista.desactivarBtnEdicion()
        for paso in pasos:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, str(paso[0]))
            self.__vista.agregar_elemento_tabla(i, 1, str(paso[1]))
            self.__vista.agregar_elemento_tabla(i, 2, str(paso[2]))
            self.__vista.agregar_elemento_tabla(i, 3, str(paso[3]))
            self.__vista.agregar_elemento_tabla(i, 4, str(paso[4]))
        self.__vista.tabla.resizeColumnsToContents()

    def cambVar(self):
        selec = self.__vista.mostrarAdvertencia("Si cambia de Variante perderá todas las calificaciones que había hecho en la anterior variante\n¿Desea Continuar?")
        if selec:
            preg = PreguntaGen(self.__preg_esp.fecha, self.__preg_esp.no_pregunta, 0)
            var = self.__vista.valor_variante
            pasos = self.__rep.obtenerPasoGen(preg, var)
            for paso in pasos:
                paso_esp = PasoEsp(self.__preg_esp.est_id, paso.obtener_elemento().fecha, paso.obtener_elemento().no_paso, var, paso.obtener_elemento().no_pregunta, 0)
                self.__rep.insertarPasoEsp(paso_esp)
            self.cargarDatos()
        else:
            self.__vista.desactivarCambVar()
            self.__vista.variante_selec.setCurrentText(self.__rep.obtenerVarPregEsp(self.__preg_esp))
            self.__vista.activarCambVar()

    def conf_var(self):
        self.__vista.desactivarCambVar()
        preg = PreguntaGen(self.__preg_esp.fecha, self.__preg_esp.no_pregunta, 0)
        variantes = self.__rep.variantePreg(preg)
        self.__vista.valor_variante = variantes
        self.__vista.variante_selec.setCurrentText(self.__rep.obtenerVarPregEsp(self.__preg_esp))
        self.__vista.activarCambVar()

    def rellenarCalXTabla(self):
        fila_select = self.__vista.tabla.currentRow()
        if fila_select != -1: 
            self.__vista.valor_cal = float(self.__vista.tabla.item(fila_select, 1).text())
        self.__vista.activarBtnEdicion()

    def editarCalPaso(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            paso = self.__pasos.nodo_en(fila_select).obtener_elemento()
            paso_esp = PasoEsp(paso.est_id, paso.fecha, paso.no_paso, paso.variante, paso.no_pregunta, self.__vista.valor_cal)
            self.__rep.actualizarPasoEsp(paso, paso_esp)
            self.cargarDatos()
        except Exception as error:
            self.__vista.mostrarError(str(error))