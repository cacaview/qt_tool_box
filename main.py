import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI import *
from web import *

class myMainWindow(Ui_mainWindow,QMainWindow):
    def __init__(self):
        super(Ui_mainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.conn)
        self.pushButton_2.clicked.connect(self.conn2)
        self.pushButton_3.clicked.connect(self.conn3)
        self.pushButton_4.clicked.connect(self.conn4)
        self.pushButton_5.clicked.connect(self.conn5)
        self.pushButton_6.clicked.connect(self.conn6)
        self.pushButton_7.clicked.connect(self.conn7)
        self.pushButton_8.clicked.connect(self.conn8)
        self.pushButton_9.clicked.connect(self.conn9)
        self.pushButton_10.clicked.connect(self.conn10)
        self.pushButton_11.clicked.connect(self.conn11)
        self.pushButton_12.clicked.connect(self.conn12)
        self.pushButton_13.clicked.connect(self.conn13)
        self.pushButton_14.clicked.connect(self.conn14)

    def conn(self):     #短视频
        f = open("./lib/theurl.txt", "w")
        f.write("https://watermark.liumingye.cn/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn2(self):        #电子书
        f = open("./lib/theurl.txt", "w")
        f.write("https://epub.liumingye.cn/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn3(self):        #分享文本
        f = open("./lib/theurl.txt", "w")
        f.write("https://paste.liumingye.cn/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn4(self):    #格式互转
        f = open("./lib/theurl.txt", "w")
        f.write("https://convertio.co/zh/document-converter/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn5(self):        #新番
        f = open("./lib/theurl.txt", "w")
        f.write("https://bgm.liumingye.cn/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn6(self):        #b站格式互转
        f = open("./lib/theurl.txt", "w")
        f.write("https://tool.liumingye.cn/avbv")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn7(self):        #谷歌翻译
        f = open("./lib/theurl.txt", "w")
        f.write("https://translate.google.cn")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn8(self):
        os.system("start runvideo.bat")

    def conn9(self):
        f = open("./lib/theurl.txt", "w")
        f.write("https://lab.liumingye.cn/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn10(self):
        f = open("./lib/theurl.txt", "w")
        f.write("https://toolwa.com/ps/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn11(self):
        f = open("./lib/theurl.txt", "w")
        f.write("http://lab.mkblog.cn/FCGames/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn12(self):
        os.system("start runcat.bat")

    def conn13(self):
        f = open("./lib/theurl.txt", "w")
        f.write("https://devhints.io/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

    def conn14(self):
        f = open("./lib/theurl.txt", "w")
        f.write("https://cn.bing.com/")
        f.close()
        main_demo = MainDemo()
        main_demo.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maingui = myMainWindow()       #主窗口
    maingui.show()

    sys.exit(app.exec_())