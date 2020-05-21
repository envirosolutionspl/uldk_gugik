# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UldkGugik
                                 A QGIS plugin
 Wtyczka pozwala na pobieranie geometrii granic działek katastralnych, obrębów, gmin, powiatów i województw.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Envirosolutions Sp. z o.o. - Michał Włoga & Alicja Konkol
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
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QVariant, Qt
from PyQt5.QtGui import QIcon, QPixmap, QKeySequence
from PyQt5.QtWidgets import QAction, QToolBar, QShortcut
from qgis.gui import QgsMessageBar, QgsMapToolEmitPoint, QgsDockWidget
from qgis.core import Qgis, QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject, QgsField, \
    QgsCoordinateReferenceSystem, QgsPoint, QgsCoordinateTransform, QgsMessageLog
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .uldk_gugik_dialog import UldkGugikDialog
from .uldk_gugik_dialog_parcel import UldkGugikDialogParcel
import os.path
from . import utils, uldk_api, uldk_xy, uldk_parcel

"""Wersja wtyczki"""
plugin_version = '1.1.1 RedOak'
plugin_name = 'ULDK GUGiK'

class UldkGugik:
    """QGIS Plugin Implementation."""
    nazwy_warstw = {1:"dzialki_ew_uldk", 2:"obreby_ew_uldk", 3:"gminy_uldk", 4:"powiaty_uldk", 5:"wojewodztwa_uldk"}
    crs = 2180

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        #DialogOnTop

        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'UldkGugik_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&EnviroSolutions')

        #toolbar
        self.toolbar = self.iface.mainWindow().findChild(QToolBar, 'EnviroSolutions')
        if not self.toolbar:
            self.toolbar = self.iface.addToolBar(u'EnviroSolutions')
            self.toolbar.setObjectName(u'EnviroSolutions')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.canvas = self.iface.mapCanvas()
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        self.clickTool.canvasClicked.connect(self.canvasClicked)

        self.dlg = UldkGugikDialog()

        # skrot klawiszowy
        self.shortcut = QShortcut(iface.mainWindow())
        self.shortcut.setKey(QKeySequence(Qt.ALT + Qt.Key_D))
        self.shortcut.activated.connect(self.shortcut_activated)


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('UldkGugik', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            #self.iface.addToolBarIcon(action)
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/uldk_gugik/images/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Usługa Lokalizacji Działek Katastralnych (ULDK)'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True
        #self.dock = UldkGugikDialog()
        #self.iface.addDockWidget(Qt.RigthDockWidgetArea, self.dock)


        # Inicjacja grafik
        self.dlg.img_main.setPixmap(QPixmap(':/plugins/uldk_gugik/images/icon_uldk2.png'))
        self.dlg.img_tab2.setPixmap(QPixmap(':/plugins/uldk_gugik/images/coords.png'))

        # rozmiar okna
        self.dlg.setFixedSize(self.dlg.size())

        # informacje o wersji
        self.dlg.setWindowTitle('%s %s' % (plugin_name, plugin_version))
        self.dlg.lbl_pluginVersion.setText('%s %s' % (plugin_name, plugin_version))

        #eventy
        self.dlg.btn_download_tab1.clicked.connect(self.btn_download_tab1_clicked)
        self.dlg.btn_download_tab2.clicked.connect(self.btn_download_tab2_clicked)
        self.dlg.btn_download_tab3.clicked.connect(self.btn_download_tab3_clicked)
        self.dlg.btn_frommap.clicked.connect(self.btn_frommap_clicked)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&EnviroSolutions'),
                action)
            # self.iface.removeToolBarIcon(action)
            self.toolbar.removeAction(action)

    def run(self):
        """Run method that performs all the real work"""

        # show the dialog
        self.dlg.show()
        self.dlg.projectionWidget.setCrs(QgsCoordinateReferenceSystem(int(self.crs), QgsCoordinateReferenceSystem.EpsgCrsId))



    def btn_download_tab1_clicked(self):


        self.objectType = self.checkedFeatureType()

        objid = self.dlg.edit_id.text().strip()

        if not objid:
            self.iface.messageBar().pushMessage("Błąd formularza:",
                                                'musisz wpisać identyfikator',
                                                level=Qgis.Warning, duration=10)
        elif utils.isInternetConnected():
            self.performRequest(pid=objid)
            self.dlg.hide()

        else:
            self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                'brak połączenia z internetem',
                                                level=Qgis.Critical, duration=10)

    def btn_download_tab2_clicked(self):
        """pobieranie według X i Y wpisanych ręcznie"""
        # self.crs = QgsProject.instance().crs().authid().split(":")[1]
        srid = self.dlg.projectionWidget.crs().authid().split(":")[1]
        self.downloadByXY(srid)

    def downloadByXY(self, srid):
        """pobranie według X i Y i SRID"""

        self.objectType = self.checkedFeatureType()

        objX = self.dlg.doubleSpinBoxX.text().strip()
        objY = self.dlg.doubleSpinBoxY.text().strip()

        if not objX:
            self.iface.messageBar().pushMessage("Błąd formularza:",
                                                'musisz wpisać współrzędną X',
                                                level=Qgis.Warning, duration=10)

        if not objY:
            self.iface.messageBar().pushMessage("Błąd formularza:",
                                                'musisz wpisać współrzędną Y',
                                                level=Qgis.Warning, duration=10)

        elif utils.isInternetConnected():
            self.performRequestXY(x=objX, y=objY, srid=srid)
            self.dlg.hide()

        else:
            self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                'brak połączenia z internetem',
                                                level=Qgis.Critical, duration=10)
    def shortcut_activated(self):
        self.canvas.setMapTool(self.clickTool)


    def btn_frommap_clicked(self):
        self.canvas.setMapTool(self.clickTool)
        self.dlg.hide()

    def canvasClicked(self, point):
        """kliknięte na mapie"""
        self.canvas.unsetMapTool(self.clickTool)
        self.dlg.doubleSpinBoxX.setValue(point.x())
        self.dlg.doubleSpinBoxY.setValue(point.y())

        coords = "{}, {}".format(point.x(), point.y())
        QgsMessageLog.logMessage(str(coords), 'ULDK')
        srid = QgsProject.instance().crs().authid().split(":")[1]
        self.downloadByXY(srid)

    def btn_download_tab3_clicked(self):
        self.objectType = self.checkedFeatureType()

        objRegion = self.dlg.edit_id_2.text().strip()

        objParcel = self.dlg.edit_id_3.text().strip()

        if not objRegion:
            self.iface.messageBar().pushMessage("Błąd formularza:",
                                                'musisz wpisać obręb',
                                                level=Qgis.Warning, duration=10)

        if not objParcel:
            self.iface.messageBar().pushMessage("Błąd formularza:",
                                                'musisz wpisać numer działki',
                                                level=Qgis.Warning, duration=10)

        elif utils.isInternetConnected():
            self.performRequestParcel(region=objRegion, parcel=objParcel)
            self.dlg.hide()

        else:
            self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                'brak połączenia z internetem',
                                                level=Qgis.Critical, duration=10)

    def performRequestParcel(self, region, parcel):

        self.crs = QgsProject.instance().crs().authid().split(":")[1]

        name = region + ' ' + parcel

        result = uldk_parcel.getParcelById(name, self.crs)
        if result is None:
            self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                'API nie zwróciło obiektu dla id %s' % name,
                                                level=Qgis.Critical, duration=10)
            return

        res = result.split("|")
        if res[0] == '':
            self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                'API nie zwróciło geometrii dla id %s' % name,
                                                level=Qgis.Critical, duration=10)
            return
        wkt = res [0]
        teryt = res [1]
        parcel = res [2]
        region = res [3]
        commune = res [4]
        county = res [5]
        voivodeship = res [6]
        # print(teryt, parcel, region, commune, county, voivodeship)

        # layer
        nazwa = self.nazwy_warstw[self.objectType]
        layers = QgsProject.instance().mapLayersByName(nazwa)
        geom = QgsGeometry().fromWkt(wkt)
        feat = QgsFeature()
        feat.setGeometry(geom)
        canvas = self.iface.mapCanvas()

        if layers:
            # jezeli istnieje to dodaj obiekt do warstwy
            layer = layers[0]
        else:
            # jezeli nie istnieje to stworz warstwe
            epsg = "Polygon?crs=EPSG:" + self.crs
            layer = QgsVectorLayer(epsg, nazwa, "memory")
            QgsProject.instance().addMapLayer(layer)

        box = feat.geometry().boundingBox()

        canvas.setExtent(box)
        provider = layer.dataProvider()
        provider.addFeature(feat)
        layer.updateExtents()
        canvas.refresh()

        counter = layer.featureCount()
        # add attributes
        if not layers:
            identyfikatorField = QgsField('identyfikator', QVariant.String, len=30)
            provider.addAttributes([identyfikatorField])

            voivField = QgsField('województwo', QVariant.String, len=30)
            provider.addAttributes([voivField])

            conField = QgsField('powiat', QVariant.String, len=30)
            provider.addAttributes([conField])

            comField = QgsField('gmina', QVariant.String, len=30)
            provider.addAttributes([comField])

            regField = QgsField('obręb', QVariant.String, len=30)
            provider.addAttributes([regField])
            layer.updateFields()

            parField = QgsField('numer', QVariant.String, len=30)
            provider.addAttributes([parField])
            layer.updateFields()

            layer.updateFields()
            counter = 1

        idx = layer.fields().indexFromName('identyfikator')
        attrMap = {counter: {idx: teryt}}
        provider.changeAttributeValues(attrMap)

        voiv = layer.fields().indexFromName('województwo')
        attrMap = {counter: {voiv: voivodeship}}
        provider.changeAttributeValues(attrMap)

        if parcel is not None:
            par = layer.fields().indexFromName('numer')
            attrMap = {counter: {par: parcel}}
            provider.changeAttributeValues(attrMap)

        if region is not None:
            reg = layer.fields().indexFromName('obręb')
            attrMap = {counter: {reg: region}}
            provider.changeAttributeValues(attrMap)
        if commune is not None:
            com = layer.fields().indexFromName('gmina')
            attrMap = {counter: {com: commune}}
            provider.changeAttributeValues(attrMap)

        if county is not None:
            con = layer.fields().indexFromName('powiat')
            attrMap = {counter: {con: county}}
            provider.changeAttributeValues(attrMap)

        self.iface.messageBar().pushMessage("Sukces:",
                                            'pobrano obrys obiektu %s' % (name),
                                            level=Qgis.Success, duration=10)

    def performRequest(self, pid):

        self.crs = QgsProject.instance().crs().authid().split(":")[1]

        if self.objectType == 1:
            if uldk_api.getParcelById(pid, self.crs) is None:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return

            res = uldk_api.getParcelById(pid, self.crs).split("|")
            if res[0] == '':
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło geometrii dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            wkt = res [0]
            teryt = res [1]
            parcel = res [2]
            region = res [3]
            commune = res [4]
            county = res [5]
            voivodeship = res [6]
            # print(teryt, parcel, region, commune, county, voivodeship)

        elif self.objectType == 2:
            if uldk_api.getRegionById(pid, self.crs) is None and self.objectType == 2:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = uldk_api.getRegionById(pid, self.crs).split("|")
            if res[0] == '':
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło geometrii dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = res[2]
            commune = res[3]
            county = res[4]
            voivodeship = res[5]
            # print(teryt, region, commune, county, voivodeship)

        elif self.objectType == 3:
            if uldk_api.getCommuneById(pid, self.crs) is None and self.objectType == 3:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = uldk_api.getCommuneById(pid, self.crs).split("|")
            if res[0] == '':
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło geometrii dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = None
            commune = res[2]
            county = res[3]
            voivodeship = res[4]
            # print(teryt, commune, county, voivodeship)

        elif self.objectType == 4:
            if uldk_api.getCountyById(pid, self.crs) is None and self.objectType == 4:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = uldk_api.getCountyById(pid, self.crs).split("|")
            if res[0] == '':
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło geometrii dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = None
            commune = None
            county = res[2]
            voivodeship = res[3]
            # print(teryt, county, voivodeship)
        elif self.objectType == 5:
            if uldk_api.getVoivodeshipById(pid, self.crs) is None and self.objectType == 5:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = uldk_api.getVoivodeshipById(pid, self.crs).split("|")
            if res[0] == '':
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło geometrii dla id %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = None
            commune = None
            county = None
            voivodeship = res[2]
            # print(teryt, voivodeship)

        # layer
        nazwa = self.nazwy_warstw[self.objectType]
        layers = QgsProject.instance().mapLayersByName(nazwa)
        geom = QgsGeometry().fromWkt(wkt)
        feat = QgsFeature()
        feat.setGeometry(geom)
        canvas = self.iface.mapCanvas()

        if layers:
            # jezeli istnieje to dodaj obiekt do warstwy
            layer = layers[0]
        else:
            # jezeli nie istnieje to stworz warstwe
            epsg = "Polygon?crs=EPSG:" + self.crs
            layer = QgsVectorLayer(epsg, nazwa, "memory")
            QgsProject.instance().addMapLayer(layer)

        box = feat.geometry().boundingBox()

        canvas.setExtent(box)
        provider = layer.dataProvider()
        provider.addFeature(feat)
        layer.updateExtents()
        canvas.refresh()

        counter = layer.featureCount()
        # add attributes
        if not layers:
            identyfikatorField = QgsField('identyfikator', QVariant.String, len=30)
            provider.addAttributes([identyfikatorField])

            voivField = QgsField('województwo', QVariant.String, len=30)
            provider.addAttributes([voivField])

            if self.objectType == 4 or self.objectType == 3 or self.objectType == 2 or self.objectType == 1:
                conField = QgsField('powiat', QVariant.String, len=30)
                provider.addAttributes([conField])

            if self.objectType == 3 or self.objectType == 2 or self.objectType == 1:
                comField = QgsField('gmina', QVariant.String, len=30)
                provider.addAttributes([comField])

            if self.objectType == 2 or self.objectType == 1:
                regField = QgsField('obręb', QVariant.String, len=30)
                provider.addAttributes([regField])
                layer.updateFields()

            if self.objectType == 1:
                parField = QgsField('numer', QVariant.String, len=30)
                provider.addAttributes([parField])
                layer.updateFields()

            layer.updateFields()
            counter = 1

        idx = layer.fields().indexFromName('identyfikator')
        attrMap = {counter: {idx: teryt}}
        provider.changeAttributeValues(attrMap)

        voiv = layer.fields().indexFromName('województwo')
        attrMap = {counter: {voiv: voivodeship}}
        provider.changeAttributeValues(attrMap)

        if parcel is not None:
            par = layer.fields().indexFromName('numer')
            attrMap = {counter: {par: parcel}}
            provider.changeAttributeValues(attrMap)

        if region is not None:
            reg = layer.fields().indexFromName('obręb')
            attrMap = {counter: {reg: region}}
            provider.changeAttributeValues(attrMap)
        if commune is not None:
            com = layer.fields().indexFromName('gmina')
            attrMap = {counter: {com: commune}}
            provider.changeAttributeValues(attrMap)

        if county is not None:
            con = layer.fields().indexFromName('powiat')
            attrMap = {counter: {con: county}}
            provider.changeAttributeValues(attrMap)

        self.iface.messageBar().pushMessage("Sukces:",
                                            'pobrano obrys obiektu %s' % (pid),
                                            level=Qgis.Success, duration=10)

    def performRequestXY(self, x, y, srid):

        x = float(x.replace(",", "."))
        y = float(y.replace(",", "."))
        requestPoint = QgsPoint(x, y)
        QgsMessageLog.logMessage(str(srid), 'ULDK')

        if srid != '2180':
            sourceCrs = QgsCoordinateReferenceSystem.fromEpsgId(int(srid))
            destCrs = QgsCoordinateReferenceSystem.fromEpsgId(2180)
            tr = QgsCoordinateTransform(sourceCrs, destCrs, QgsProject.instance())
            requestPoint.transform(tr)

        pid = str(requestPoint.x()) + "," + str(requestPoint.y())

        # layer
        nazwa = self.nazwy_warstw[self.objectType]

        layers = QgsProject.instance().mapLayersByName(nazwa)

        if self.objectType == 1:# działka
            resp = uldk_xy.getParcelByXY(xy=pid, srid='2180')
            if not resp:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla współrzędnych %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = resp.split("|")
            wkt = res[0]
            teryt = res[1]
            parcel = res[2]
            region = res[3]
            commune = res[4]
            county = res[5]
            voivodeship = res[6]
            print(teryt, parcel, region, commune, county, voivodeship)

        elif self.objectType == 2:
            resp = uldk_xy.getRegionByXY(xy=pid, srid='2180')
            if not resp:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla dla współrzędnych %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = resp.split("|")
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = res[2]
            commune = res[3]
            county = res[4]
            voivodeship = res[5]
            print(teryt, region, commune, county, voivodeship)

        elif self.objectType == 3:
            resp = uldk_xy.getCommuneByXY(pid, srid)
            if not resp:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla współrzędnych %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = resp.split("|")
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = None
            commune = res[2]
            county = res[3]
            voivodeship = res[4]
            print(teryt, commune, county, voivodeship)

        elif self.objectType == 4:
            resp = uldk_xy.getCountyByXY(pid, srid)
            if not resp:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla współrzędnych %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = resp.split("|")
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = None
            commune = None
            county = res[2]
            voivodeship = res[3]
            print(teryt, county, voivodeship)

        elif self.objectType == 5:
            resp = uldk_xy.getVoivodeshipByXY(pid, srid)
            if not resp:
                self.iface.messageBar().pushMessage("Nie udało się pobrać obiektu:",
                                                    'API nie zwróciło obiektu dla współrzędnych %s' % pid,
                                                    level=Qgis.Critical, duration=10)
                return
            res = resp.split("|")
            wkt = res[0]
            teryt = res[1]
            parcel = None
            region = None
            commune = None
            county = None
            voivodeship = res[2]
            print(teryt, voivodeship)

        feat = QgsFeature()
        feat.setGeometry(QgsGeometry().fromWkt(wkt))
        canvas = self.iface.mapCanvas()

        if layers:
            # jezeli istnieje to dodaj obiekt do warstwy
            layer = layers[0]

        else:
            # jezeli nie istnieje to stworz warstwe
            source = "Polygon?crs=EPSG:2180"
            layer = QgsVectorLayer(source, nazwa, "memory")
            QgsProject.instance().addMapLayer(layer)

        projectCrs = QgsProject.instance().crs().authid().split(":")[1]
        if projectCrs != '2180':
            sourceCrs = QgsCoordinateReferenceSystem.fromEpsgId(2180)
            destCrs = QgsCoordinateReferenceSystem.fromEpsgId(int(projectCrs))
            tr = QgsCoordinateTransform(sourceCrs, destCrs, QgsProject.instance())
            box = tr.transform(feat.geometry().boundingBox())
        else:
            box = feat.geometry().boundingBox()

        canvas.setExtent(box)
        canvas.refresh()
        provider = layer.dataProvider()
        provider.addFeature(feat)

        featId = layer.featureCount()

        if not layers:
            identyfikatorField = QgsField('identyfikator', QVariant.String, len=30)
            provider.addAttributes([identyfikatorField])

            voivField = QgsField('województwo', QVariant.String, len=30)
            provider.addAttributes([voivField])

            if self.objectType == 4 or self.objectType == 3 or self.objectType == 2 or self.objectType == 1:
                conField = QgsField('powiat', QVariant.String, len=30)
                provider.addAttributes([conField])

            if self.objectType == 3 or self.objectType == 2 or self.objectType == 1:
                comField = QgsField('gmina', QVariant.String, len=30)
                provider.addAttributes([comField])

            if self.objectType == 2 or self.objectType == 1:
                regField = QgsField('obręb', QVariant.String, len=30)
                provider.addAttributes([regField])

            if self.objectType == 1:
                parField = QgsField('numer', QVariant.String, len=30)
                provider.addAttributes([parField])

            layer.updateFields()
            featId = 1

        idx = layer.fields().indexFromName('identyfikator')
        attrMap = {featId: {idx: teryt}}
        provider.changeAttributeValues(attrMap)

        voiv = layer.fields().indexFromName('województwo')
        attrMap = {featId: {voiv: voivodeship}}
        provider.changeAttributeValues(attrMap)

        if parcel:
            par = layer.fields().indexFromName('numer')
            attrMap = {featId: {par: parcel}}
            provider.changeAttributeValues(attrMap)

        if region:
            reg = layer.fields().indexFromName('obręb')
            attrMap = {featId: {reg: region}}
            provider.changeAttributeValues(attrMap)
        if commune:
            com = layer.fields().indexFromName('gmina')
            attrMap = {featId: {com: commune}}
            provider.changeAttributeValues(attrMap)

        if county:
            con = layer.fields().indexFromName('powiat')
            attrMap = {featId: {con: county}}
            provider.changeAttributeValues(attrMap)

        self.iface.messageBar().pushMessage("Sukces:",
                                            'pobrano obrys obiektu %s' % teryt,
                                            level=Qgis.Success, duration=10)

    def checkedFeatureType(self):
        dlg = self.dlg
        if dlg.rdb_dz.isChecked():
            return 1
        elif dlg.rdb_ob.isChecked():
            return 2
        elif dlg.rdb_gm.isChecked():
            return 3
        elif dlg.rdb_pw.isChecked():
            return 4
        elif dlg.rdb_wo.isChecked():
            return 5
        else:
            return 0
