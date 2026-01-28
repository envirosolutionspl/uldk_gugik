from urllib.parse import urlencode
from qgis.PyQt.QtNetwork import QNetworkReply, QNetworkRequest
from qgis.PyQt.QtCore import QEventLoop, QUrl
from qgis.core import QgsMessageLog, Qgis, QgsNetworkAccessManager
from .https_adapter import getLegacySession

if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


class Request:
    def __init__(self, params,object_type, **kwargs):
        self.params = params
        self._data = None
        self.url = "https://uldk.gugik.gov.pl/"
        self.session = getLegacySession()

        self.teryt = kwargs.get('teryt', None)
        self.object_type = object_type
        
        # Utworzenie loop PRZED wywołaniem request
        self.loop = QEventLoop()
        self.reply = None
        
        self.getRequest()
        self.loop.exec()

    def getRequest(self):
        try:
            final_url = f"{self.url}?{urlencode(self.params)}"
            self.reply = self.session.get(final_url)
            if not self.reply:
                return
        except Exception as e:
            return

        try:
            is_finished = self.reply.isFinished()
            if is_finished:
                self.handleReply()
                return
        except Exception as e:
            pass
        
        def handleReply():
            reply = self.reply
            try:
                error_val = reply.error()
                if hasattr(QNetworkReply, 'NetworkError'):
                    no_err = QNetworkReply.NetworkError.NoError  # Qt6
                    is_no_error = (error_val == no_err)  # W Qt6 porównujemy enumy bezpośrednio
                else:
                    no_err = QNetworkReply.NoError  # Qt5
                    is_no_error = (int(error_val) == int(no_err))  # W Qt5 konwertujemy na int
                
                if is_no_error:
                    read_data = reply.readAll()
                    if hasattr(read_data, 'data'):
                        returned_data = read_data.data().decode('utf-8')
                    else:
                        returned_data = bytes(read_data).decode('utf-8')
                    
                    if not returned_data or len(returned_data.strip()) == 0:
                        self._data = None
                    else:
                        for line in returned_data.split('\n'):
                            if len(line) < 3 or line == "-1 brak wyników" or line.find("XML")>-1 or line.find("błęd")>-1:
                                continue
                            if ";" in line:
                                polygon = line.split(';')[1]
                                if not self.teryt:
                                    self._data = polygon
                                    break
                                
                                try:
                                    if self.object_type in [1, 6]:
                                        teryt = polygon.split('|')[1].split('.')[0]
                                    elif self.object_type == 2:
                                        if polygon.split('|')[1].find(".") > -1:
                                            teryt = polygon.split('|')[1].split('.')[0]
                                        else:
                                            continue
                                    else:
                                        teryt = polygon.split('|')[1]

                                    if self.teryt and teryt[:-4] == self.teryt[:-4]:
                                        # jeżeli wybór przezXY lub teryt z formularza == teryt otrzymany z odpowiedzi
                                        self._data = polygon
                                        break
                                except (IndexError, AttributeError):
                                    continue

                            else:
                                if not self.teryt:
                                    self._data = line
                                    break

                                try:
                                    if self.object_type in [1, 6]:
                                        teryt = line.split('|')[1].split('.')[0]
                                    elif self.object_type == 2:
                                        if line.split('|')[1].find(".") > -1:
                                            teryt = line.split('|')[1].split('.')[0]
                                        else:
                                            continue
                                    else:
                                        teryt = line.split('|')[1].split('.')[0]
                                    
                                    if self.teryt and teryt[:-4] == self.teryt[:-4]:
                                        self._data = line
                                        break
                                except (IndexError, AttributeError):
                                    continue

                else:
                    self._data = None
            except Exception:
                self._data = None
            finally:
                if self.loop.isRunning():
                    self.loop.quit()
                reply.deleteLater()
        
        if self.reply:
            self.reply.finished.connect(handleReply)

    @property
    def data(self):
        return self._data