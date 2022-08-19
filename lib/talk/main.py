import os
import sys

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QMainWindow
from PyQt5.QtGui import QIcon
from GUI import *


class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.talk)


    def talk(self):
        str = self.lineEdit.text()
        self.lineEdit.clear()
        b = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + str)
        c = b.text
        str1 = c[23:]
        mylen = len(str1)
        thelen = mylen - 2
        str2 = str1[:thelen]
        print(str2)
        f = open("talk.txt", "a")
        str3 = "你：" + str + "\n"
        str4 = "机器人：" + str2 + "\n"
        f.write(str3)
        f.write(str4)
        f.close()

        r = open("talk.txt", "r")
        #print(r.read())
        self.textBrowser.setText(r.read())


    def closeEvent(self, event):
        f = open("talk.txt", "w")
        f.write("")
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    talk_Window = MainWindow()
    talk_Window.show()

    sys.exit(app.exec_())
