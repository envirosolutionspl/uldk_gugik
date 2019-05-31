# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uldk_gugik_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UldkGugikDialogBase(object):
    def setupUi(self, UldkGugikDialogBase):
        UldkGugikDialogBase.setObjectName("UldkGugikDialogBase")
        UldkGugikDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(UldkGugikDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")

        self.retranslateUi(UldkGugikDialogBase)
        self.button_box.accepted.connect(UldkGugikDialogBase.accept)
        self.button_box.rejected.connect(UldkGugikDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(UldkGugikDialogBase)

    def retranslateUi(self, UldkGugikDialogBase):
        _translate = QtCore.QCoreApplication.translate
        UldkGugikDialogBase.setWindowTitle(_translate("UldkGugikDialogBase", "Usługa Lokalizacji Działek Katastralnych"))


