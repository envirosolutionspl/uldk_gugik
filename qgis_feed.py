from qgis.core import (QgsNewsFeedParser, QgsSettings, QgsNewsFeedModel, 
                       QgsMessageLog, QgsApplication)
from qgis.PyQt.QtCore import QUrl
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog, QComboBox, QPushButton

import re
import os
import unicodedata

from .constants import INDUSTRIES

class QgisFeed:
    def __init__(self, selected_industry, plugin_name):
        self.s = QgsSettings()
        # self.envirosolutionsFeedPattern = re.compile('core/NewsFeed/httpsqgisfeedenvirosolutionspl/\d+/\w+')
        self.industries_dict = INDUSTRIES

        self.industry_decoded = [key for key, val in self.industries_dict.items() if val == selected_industry]
        self.plugin_name_slug = self.create_slug(plugin_name)

        self.es_url = "https://qgisfeed.envirosolutions.pl/" if len(self.industry_decoded) == 0 else f"https://qgisfeed.envirosolutions.pl/?industry={self.industry_decoded[0]}&plugin={self.plugin_name_slug}"
        self.parser = QgsNewsFeedParser(
            feedUrl= QUrl(self.es_url)
        )
        self.industry_url_short = self.shortenUrl(self.es_url)
        self.envirosolutionsFeedPattern_old = re.compile(f"core/NewsFeed/{self.industry_url_short}")
        self.envirosolutionsFeedPattern_new = re.compile(f"app/news-feed/items/{self.industry_url_short}")

        self.parser.fetched.connect(self.registerFeed)
        
    def shortenUrl(self, url):
        """
        Funkcja przetwarza zapisany adres qgisfeed'a 
        na forme zapisana w qgis settingsach
        """
        
        return re.sub(r'://|\.|:|/\?|=|&|-', '', url)

    def create_slug(self, text):
        """
        This function makes slug from a random text
        """
        slug = self.normalizeString(text)
        slug = re.sub(r'[^a-z0-9\s-]', '', slug.lower())  # Remove non-alphanumeric characters except spaces and hyphens
        slug = re.sub(r'[\s]+', '-', slug)  # Replace spaces with hyphens
        
        return slug.strip('-')

    def normalizeString(self, text):
        return ''.join(part for part in unicodedata.normalize('NFD', text)
                       if unicodedata.category(part) != 'Mn')

    def registerFeed(self):
        """
        Function registers QGIS Feed
        """
        print("New url: ",self.industry_url_short)
        QgsMessageLog.logMessage('Registering feed')
        for key in self.s.allKeys():
            if self.envirosolutionsFeedPattern_old.match(key) or self.envirosolutionsFeedPattern_new.match(key):
                finalKey = re.sub(r'(\d+)', r'9999\1', key.replace(self.industry_url_short, 'httpsfeedqgisorg'))
                self.s.setValue(finalKey, self.s.value(key))

            # ponizszy fragment odpowiada za mozliwosc ciaglego wyswietlania wiadomosci
            # przy wlaczeniu qgis za kazdym razem

            check_fetch = self.checkIsFetchTime()
            if check_fetch is True: self.s.remove(key)

    def removeDismissed(self):
        """
        Function checks whether there was already initialized QGIS Feed
        """

        for key in self.s.allKeys():
            if self.envirosolutionsFeedPattern_old.match(key) or self.envirosolutionsFeedPattern_new.match(key):
                # sprawdz czy jest odpowiadajacy w qgis
                if self.s.contains(re.sub(r'(\d+)', r'9999\1', key.replace(self.industry_url_short, 'httpsfeedqgisorg'))):
                    self.s.remove(key)
                self.s.remove(key)

    def checkIsFetchTime(self):
        """
        Function check if the fetch time from QGIS Feed was already registered
        """

        return self.s.contains(f"core/NewsFeed/{self.industry_url_short}/lastFetchTime") \
                or self.s.contains(f"app/news-feed/items/{self.industry_url_short}/last-fetch-time")

    def initFeed(self):
        """
        Function is a built in QGIS class and it is responsible for firing QGIS Feed
        """

        check_fetch = self.checkIsFetchTime()
        if check_fetch is True: self.removeDismissed()
        self.parser.fetch()
        

class QgisFeedDialog(QDialog):
    def __init__(self, parent=None):
        super(QgisFeedDialog, self).__init__(parent)
        self.ui_file_path = os.path.join(os.path.dirname(__file__),'ui','qgis_feed.ui')
        uic.loadUi(self.ui_file_path, self)
        
        self.comboBox = self.findChild(QComboBox, 'comboBox')
        self.pushButton = self.findChild(QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.onSaveClicked)

        self.loadPreviousSelection()

    def loadPreviousSelection(self):
        settings = QgsSettings()
        previous_selection = settings.value("selected_industry")
        if previous_selection:
            index = self.comboBox.findText(previous_selection)
            if index != -1:
                self.comboBox.setCurrentIndex(index)
            self.hide()  

    def onSaveClicked(self):
        #zapisz wybraną branżę
        selected_industry = self.comboBox.currentText()
        settings = QgsSettings()
        settings.setValue("selected_industry", selected_industry)  
        self.accept()  

# class QgisFeedDB:
    
#     def __init__(self):
#         self.db = QgsApplication.qgisUserDatabaseFilePath()
#         self.tbl_name = "qgis_feed_vals"

#     def createConnection(self):
#         print(self.db)
#         connection = sql.connect(self.db)
#         cursor = connection.cursor()

#         return cursor

#     def checkTblExist(self, cursor):
#         querry = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.tbl_name}';"
#         print(f"query: {querry}")
#         res = cursor.execute(querry)

#         return res.fetchone()

#     def createUserParamsDB(self, cursor):
#         query = """
#         CREATE TABLE qgis_feed_vals(
#             id serial PRIMARY KEY,
#             industry VARCHAR(100),
#             date_insert DATE
#         );
#         """
#         cursor.execute(query)

#     def selectUserBrand(self, cursor):
#         query = f"SELECT industry from '{self.tbl_name}'"
#         cursor.execute(query)

#     def insertNecessaryVals(self, cursor, user_industry):
#         query = f"""
#         INSERT INTO {self.tbl_name}(industry, date_insert) VALUES ('{user_industry}',DATE('NOW'))
#         """
#         cursor.execute(query)

