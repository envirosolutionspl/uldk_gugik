# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UldkGugikDialog
                                 A QGIS plugin
 Wtyczka pozwala na pobieranie geometrii granic działek katastralnych, obrębów, gmin, powiatów i województw.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Michał Włoga - Envirosolutions Sp. z o.o.
        email                : office@envirosolutions.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal, QRegExp
from qgis.PyQt.QtGui import QRegExpValidator
from qgis.gui import QgsFileWidget
from qgis.core import QgsMapLayerProxyModel
from .uldk import RegionFetch

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'uldk_gugik_dialog_base.ui'))


class UldkGugikDialog(QtWidgets.QDialog, FORM_CLASS):

    closingPlugin = pyqtSignal()
    def __init__(self, parent=None):
        """Constructor."""
        super(UldkGugikDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        #self.folder_fileWidget.setStorageMode(QgsFileWidget.GetDirectory)

        # ULDK
        self.setup_signals()
        self.powiatDictionary = {}
        self.gminaDictionary = {}
        self.obrebDictionary = {}


    def setup_signals(self):
        self.wojcomboBox.currentTextChanged.connect(self.wojcomboBox_currentTextChanged)
        self.powcomboBox.currentTextChanged.connect(self.powcomboBox_currentTextChanged)
        self.gmicomboBox.currentTextChanged.connect(self.gmicomboBox_currentTextChanged)

    def fill_dialog(self):
        self.regionFetch = RegionFetch()
        wojewodztwa = self.regionFetch.wojewodztwoDict
        self.wojcomboBox.addItems(wojewodztwa.keys())
        data = {k: v for k, v in wojewodztwa.items()}
        for idx, po in enumerate(data.keys()):
            self.wojcomboBox.setItemData(idx, data[po])

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def wojcomboBox_currentTextChanged(self, text):
        self.powcomboBox.clear()
        self.handleResponseObjects("wojewodztwo", False)

        self.powiatDictionary = self.regionFetch.getPowiatDictByWojewodztwoName(text)
        data = {k: v[0] for k, v in self.powiatDictionary.items()}
        self.powcomboBox.addItems(list(self.powiatDictionary.keys()))

        for idx, po in enumerate(data.keys()):
            self.powcomboBox.setItemData(idx, data[po])

        self.handleResponseObjects("wojewodztwo", True)

    def powcomboBox_currentTextChanged(self, text):
        self.gmicomboBox.clear()
        self.handleResponseObjects("powiat", False)

        self.gminaDictionary = self.regionFetch.getGminaDictByPowiatName(text)
        self.gmicomboBox.addItems(list(self.gminaDictionary.keys()))

        self.handleResponseObjects("powiat", True)


    def gmicomboBox_currentTextChanged(self, text):
        self.obrcomboBox.clear()
        self.handleResponseObjects("gmina", False)

        self.obrebDictionary = self.regionFetch.getObrebDictByGminaName(text)
        data = {k: v for k, v in self.obrebDictionary.items()}
        self.obrcomboBox.addItems(list(self.obrebDictionary.keys()))

        for idx, ob in enumerate(data.keys()):
            self.gmicomboBox.setItemData(idx, data[ob])
            self.obrcomboBox.setItemData(idx, data[ob])

        self.handleResponseObjects("gmina", True)

    def handleResponseObjects(self, reg, param):
        if reg == "wojewodztwo":
            if param is True:
                self.wojcomboBox.setStyleSheet("QComboBox { color: black }")
                self.powcomboBox.setStyleSheet("QComboBox { color: black }")
                self.gmicomboBox.setStyleSheet("QComboBox { color: black }")
            else:
                self.wojcomboBox.setStyleSheet("QComboBox { color: gray }")
                self.powcomboBox.setStyleSheet("QComboBox { color: gray }")
                self.gmicomboBox.setStyleSheet("QComboBox { color: gray }")

            self.wojcomboBox.setEnabled(param)
            self.powcomboBox.setEnabled(param)
            self.gmicomboBox.setEnabled(param)


        elif reg == "powiat":
            if param is True:
                self.powcomboBox.setStyleSheet("QComboBox { color: black }")
                self.gmicomboBox.setStyleSheet("QComboBox { color: black }")
            else:
                self.powcomboBox.setStyleSheet("QComboBox { color: gray }")
                self.gmicomboBox.setStyleSheet("QComboBox { color: gray }")

            self.powcomboBox.setEnabled(param)
            self.gmicomboBox.setEnabled(param)

        elif reg == "gmina":
            if param is True:
                self.gmicomboBox.setStyleSheet("QComboBox { color: black }")
            else:
                self.gmicomboBox.setStyleSheet("QComboBox { color: gray }")

            self.gmicomboBox.setEnabled(param)

        if self.rdb_dz.isChecked():
            self.btn_search_tab3_2.setEnabled(param)

        self.obrcomboBox.setEnabled(param)
        self.arkcomboBox.setEnabled(param)

