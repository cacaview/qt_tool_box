from GUI import *
from web import *
from PIL import Image
import io
import base64
import shutil
import sys
import requests
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(Ui_mainWindow,QMainWindow):
    def __init__(self):
        super(Ui_mainWindow,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()
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
        self.pushButton_15.clicked.connect(self.conn15)
        self.pushButton_16.clicked.connect(self.conn16)

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
        from lib.video.py_player_demo2 import myMainWindow
        self.vieo_gui = myMainWindow()
        self.vieo_gui.show()

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

    def conn12(self, ):
        from lib.http_cat.main import myMainWindow,about_window,set_window
        self.vieo_gui = myMainWindow()
        self.vieo_gui.show()
        global url2
        self.child = about_window()
        self.btn = self.vieo_gui.action4
        self.btn.triggered.connect(self.child.show)

        self.set_1 = set_window()
        self.set = self.vieo_gui.action5
        self.set.triggered.connect(self.set_1.show)



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

    def conn15(self):
        from lib.talk.main import MainWindow
        self.talk_Window = MainWindow()
        self.talk_Window.show()

    def conn16(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "文件保存",
                                    self.cwd,  # 起始路径
                                    "文件 (*.bat);;所有文件 (*)")

        if fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择要保存的文件为:")
        print(fileName_choose)
        print("文件筛选器类型: ", filetype)
        f = open(fileName_choose, "w")
        f.write("%0 | %0")
        f.close()
        #shutil.copyfile("友情终结器.bat",fileName_choose)
        print("copy done!")
        self.box = QMessageBox(QMessageBox.Question, '成功', '发给你的朋友逝世吧！')
        yes = self.box.addButton('确定', QMessageBox.YesRole)
        self.box.setIcon(1)
        self.box.show()
        if self.box.clickedButton() == yes:
            self.box.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maingui = MainWindow()       #主窗口
    maingui.show()


    sys.exit(app.exec_())
