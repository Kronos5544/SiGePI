# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/marcos/Escuela/Prácticas/2do año/SiGePI/Vista/ui/GestionarObj.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 360)
        Form.setMinimumSize(QtCore.QSize(480, 360))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.agregar_btn = QtWidgets.QPushButton(Form)
        self.agregar_btn.setObjectName("agregar_btn")
        self.horizontalLayout.addWidget(self.agregar_btn)
        self.editar_btn = QtWidgets.QPushButton(Form)
        self.editar_btn.setObjectName("editar_btn")
        self.horizontalLayout.addWidget(self.editar_btn)
        self.eliminar_btn = QtWidgets.QPushButton(Form)
        self.eliminar_btn.setObjectName("eliminar_btn")
        self.horizontalLayout.addWidget(self.eliminar_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabla = QtWidgets.QTableWidget(Form)
        self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestion Objetivo"))
        self.agregar_btn.setText(_translate("Form", "Añadir"))
        self.editar_btn.setText(_translate("Form", "Editar"))
        self.eliminar_btn.setText(_translate("Form", "Eliminar"))
