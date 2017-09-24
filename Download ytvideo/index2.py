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

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main2.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setFixedSize(571, 332)
        self.setWindowTitle("YTDDownLoader")

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Download_Youtube_Video)
        self.pushButton_2.clicked.connect(self.Save_Browse)
        self.pushButton_3.clicked.connect(self.Get_Youtube_Video)


    def Save_Browse(self):
        save = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_2.setText(save)

    def Get_Youtube_Video(self):
        video_link = self.lineEdit.text()
        v = pafy.new(video_link)
        st = v.streams
        #print(st)
        for s in st :
            size = humanize.naturalsize(s.get_filesize()) #working
            data = '{} {} {} {}' .format(s.mediatype , s.extension , s.quality , size)
            self.comboBox.addItem(data)


    def Download_Youtube_Video(self):
        video_link = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        v = pafy.new(video_link)
        st = v.streams
        quality = self.comboBox.currentIndex()
        dwon = st[quality].download(filepath=save_location)
        QMessageBox.information(self, "Download Completed", "The Download Video Finished")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
