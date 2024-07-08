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
        copyright            : (C) 2019 by EnviroSolutions Sp. z o.o.
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
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtWidgets import QWidget

from .constants import DIALOG_MAPPING, ADMINISTRATIVE_UNITS_OBJECTS, COMBOBOX_RADIOBUTTON_MAPPING, \
    RADIOBUTTON_COMBOBOX_MAPPING
from .uldk import RegionFetch

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'uldk_gugik_dialog_base.ui'))


class UldkGugikDialog(QtWidgets.QDialog, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(UldkGugikDialog, self).__init__(parent)
        self.setupUi(self)
        self._setup_dialog()
        self._setup_signals()

    def _setup_signals(self):
        for base_combo, combo_items in ADMINISTRATIVE_UNITS_OBJECTS.items():
            fetch_func, dependent_combo = combo_items
            combo_obj = getattr(self, base_combo)
            combo_obj.currentTextChanged.connect(
                lambda _, func=fetch_func, combo=dependent_combo: self.setup_administrative_unit_obj(func, combo)
            )
        for rdbt in DIALOG_MAPPING.keys():
            getattr(self, rdbt).toggled.connect(self.setup_tab_widget)
        self.parcel_lineedit.textChanged.connect(lambda: self.btn_download_tab3.setEnabled(False))

    def _setup_dialog(self):
        self.img_main.setMargin(9)
        self.regionFetch = RegionFetch()
        self.fill_voivodeships()

    def fill_voivodeships(self):
        voivodeships_ids = self.regionFetch.wojewodztwo_dict.keys()
        voivodeships_names = self.regionFetch.wojewodztwo_dict.values()
        self.wojcomboBox.clear()
        self.wojcomboBox.addItems(voivodeships_names)
        for idx, val in enumerate(voivodeships_ids):
            self.wojcomboBox.setItemData(idx, val)
        self.wojcomboBox.setCurrentIndex(-1)

    def setup_tab_widget(self):
        rdbt_name = next(rdbt for rdbt in DIALOG_MAPPING if getattr(self, rdbt).isChecked())
        rdbt_attrs = DIALOG_MAPPING.get(rdbt_name)
        tab_title = rdbt_attrs.get('tab_title')
        self.tabWidget.setTabText(2, tab_title)
        self.tab3.findChild(QWidget).setText(tab_title)
        self.id_label.setText(f'''Wprowadź identyfikator obiektu (np. {rdbt_attrs.get('sample_id')})''')
        self.description_label.setText(rdbt_attrs.get('description_label'))
        self.parcel_lineedit.setText('')
        self.btn_search_tab3.setEnabled(rdbt_name == 'rdb_dz')
        self.btn_download_tab3.setEnabled(rdbt_name != 'rdb_dz')
        self.hide_combobxes()
        self.tabWidget.setTabVisible(2, rdbt_name != 'rdb_bu')

    def hide_combobxes(self):
        comboboxes_to_hide = []
        for rdbt, cmb in RADIOBUTTON_COMBOBOX_MAPPING.items():
            combo_obj = getattr(self, cmb)
            combo_obj.setStyleSheet("QComboBox { color: black }")
            getattr(self, cmb).setEnabled(True)
            if getattr(self, rdbt).isChecked():
                combo_idx = list(RADIOBUTTON_COMBOBOX_MAPPING).index(rdbt) + 1
                comboboxes_to_hide = list(list(RADIOBUTTON_COMBOBOX_MAPPING.values())[combo_idx:])
                break
        for combo in comboboxes_to_hide:
            combo_obj = getattr(self, combo)
            combo_obj.setStyleSheet("QComboBox { color: transparent }")
            combo_obj.setEnabled(False)

    def setup_administrative_unit_obj(self, func, dependent_combo):
        combo_obj = getattr(self, dependent_combo)
        unit_data = self.sender().currentData()
        if not unit_data:
            return
        combo_obj.clear()
        unit_dict = getattr(self.regionFetch, func)(unit_data)
        combo_obj.addItems(unit_dict.values())
        for idx, val in enumerate(unit_dict.keys()):
            combo_obj.setItemData(idx, val)
        combo_obj.setCurrentIndex(-1)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
