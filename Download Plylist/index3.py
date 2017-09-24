from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import pafy
import humanize
import urllib.request


FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main3.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setFixedSize(571, 332)
        self.setWindowTitle("PyDownLoader")

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Playlist_Download)
        self.pushButton_2.clicked.connect(self.Save_Browse)

    def Save_Browse(self):
        save = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_2.setText(save)

    def Playlist_Download(self):
        playlist_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        playlist = pafy.get_playlist(playlist_url)
        videos = playlist['items']

        os.chdir(save_location)

        if os.path.exists(str(playlist['title'])) :
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        for video in videos :
            p = video['pafy']
            best = p.getbest(preftype='mp4')
            best.download()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
