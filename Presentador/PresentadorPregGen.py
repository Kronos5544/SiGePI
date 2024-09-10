from Vista.GestionarPregGen import GestionarPregGen
from Vista.AgregarPregGen import AgregarPregGen
from Vista.ActualizarPregGen import ActualizarPregGen
from Modelo.PreguntaGen import PreguntaGen
from Presentador.PresentadorPasoGen import PresentadorPasoGen

class PresentadorPregGen:
    def __init__(self, rep, vista_princ, examen):
        self.__rep = rep
        self.__vista_princ = vista_princ
        self.__exam = examen

    def iniciar(self):
        self.__vista = GestionarPregGen(self)
        self.cargarDatos()
        self.__vista.show()
        self.__vista_princ.bloquearVentana()

    def cargarDatos(self):
        self.__vista.desactivarBtnEdicion()
        self.__preguntas = self.__rep.obtenerPreguntaGen(self.__exam)
        self.__vista.vaciarTabla()
        conf = ["No Pregunta", "Máx Calificación"]
        for var in self.__rep.varianteExamenGen(self.__exam):
            conf.append(f"Variante {var}")
        self.__vista.configurarTabla(conf)

        for preg in self.__preguntas:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, str(preg.obtener_elemento().no_pregunta))
            self.__vista.agregar_elemento_tabla(i, 1, str(preg.obtener_elemento().max_cal))
            var_comp = self.compVarCorrecta(preg.obtener_elemento())
            for ind in range(len(var_comp)):
                self.__vista.agregar_elemento_tabla(i, ind+2, var_comp[ind])
        self.__vista.tabla.resizeColumnsToContents()
        
        self.__vista.valor_cal_actual = self.__rep.calcCalExamGen(self.__exam)

    def compVarCorrecta(self, preg):
        resultado = []
        var_preg = self.__rep.variantePreg(preg)
        for var_exam in self.__rep.varianteExamenGen(self.__exam):
            if var_exam in var_preg:
                resultado.append(self.__rep.compVariante(preg, var_exam))
            else: 
                resultado.append("-")
        return resultado

    def desbloquearVentPrinc(self):
        self.__vista_princ.desbloquearVentana()

    def desbloquearVentana(self):
        self.__vista.desbloquearVentana()

    def eliminarPregGen(self):
        selec = self.__vista.mostrarAdvertencia("Eliminará la última pregunta de la lista con todos los pasos asociados a esta\n¿Está seguro que desea continuar?")
        if selec:
            self.__rep.eliminarPregGen(self.__preguntas.nodo_en(len(self.__preguntas) - 1).obtener_elemento())
            self.cargarDatos()


#-------------------Ventana Añadir Pregunta General--------------------
    def agregarPregGenVentana(self):
        self.__ag_act = AgregarPregGen(self)
        self.__ag_act.show()
        self.__vista.bloquearVentana()

    def agregarPregGen(self):
        try:
            self.__ag_act.validarDatos()
            pregunta = PreguntaGen(self.__exam.fecha, len(self.__preguntas) + 1, self.__ag_act.valor_max_cal)
            self.__rep.insertarPreguntaGen(pregunta)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))

#------------------Ventana Editar Pregunta General-------------------
    def actualizarPregGenVentana(self):
        self.__ag_act = ActualizarPregGen(self)
        self.cargarDatosActualizarPreg()
        self.__ag_act.show()
        self.__vista.bloquearVentana()

    def cargarDatosActualizarPreg(self):
        fila_selec = self.__vista.tabla.currentRow()
        self.__preg_anterior = self.__preguntas.nodo_en(fila_selec).obtener_elemento()
        self.__ag_act.valor_max_cal = self.__preg_anterior.max_cal 

    def actualizarPregGen(self):
        try:
            self.__ag_act.validarDatos()
            nueva_preg = PreguntaGen(self.__exam.fecha, self.__preg_anterior.no_pregunta, self.__ag_act.valor_max_cal)
            self.__rep.actualizarPregGen(self.__preg_anterior, nueva_preg)
            self.__ag_act.close()
        except Exception as error:
            self.__ag_act.mostrarError(str(error))

#--------------Ventana Editar Pasos------------------
    def pasosVentana(self):
        try:
            if not self.__rep.compCalExamenGen(self.__exam):
                raise Exception("Las máxima calificación de las preguntas tiene que sumar 100 antes de poder editar los pasos")
            else:
                fila_selec = self.__vista.tabla.currentRow()
                self.__preg_anterior = self.__preguntas.nodo_en(fila_selec).obtener_elemento()
                self.__paso_gen = PresentadorPasoGen(self.__rep, self.__vista, self.__preg_anterior)
                self.__paso_gen.iniciar()
                self.__vista.bloquearVentana()
        except Exception as error:
            self.__vista.mostrarError(str(error))
    