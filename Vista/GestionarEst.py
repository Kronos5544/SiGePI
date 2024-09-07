from Vista.Gestionar import Gestionar
from PyQt5.QtWidgets import QMessageBox

class GestionarEst(Gestionar):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__(self.__presentador)
        self.setWindowTitle("Gestionar Estudiantes")
        
        self.configurarTabla(["Id"])
        self.agregar_btn.clicked.connect(self.__presentador.agregarEstVentana)
        self.editar_btn.clicked.connect(self.__presentador.actualizarEstVentana)
        self.eliminar_btn.clicked.connect(self.__presentador.eliminarEst)

    def mostrarAdvertencia(self, mensaje):
            # Crear la ventana de alerta
            advertencia = QMessageBox(self)
            advertencia.setWindowTitle("Advertencia")
            advertencia.setIcon(QMessageBox.Warning)
            advertencia.setText(mensaje)
            
            # Añadir botones personalizados
            boton_aceptar = advertencia.addButton("Aceptar", QMessageBox.AcceptRole)
            boton_cancelar = advertencia.addButton("Cancelar", QMessageBox.RejectRole)
            advertencia.setDefaultButton(boton_aceptar) # Establecer Aceptar como botón predeterminado

            # Mostrar la ventana de alerta
            advertencia.exec_()

            # Evaluar la respuesta
            if advertencia.clickedButton() == boton_aceptar:
                return True
            else:
                return False

            
            
                

    
        
