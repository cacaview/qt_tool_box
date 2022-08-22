from PIL import Image
import io
import base64
import shutil
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QFileDialog,QProgressBar)
import sys
import requests
from lib.http_cat.GUI_set import *
from lib.http_cat.GUI import *
import os
from lib.http_cat.GUI_about import *

class about_window(Ui_Window,QMainWindow):
    def __init__(self):
        super(about_window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class set_window(Ui_set,QMainWindow):
    def __init__(self):
        super(set_window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push)
    def push(self):
        a = self.comboBox.currentIndex()
        if a == 0 :
            f = open("http.txt", "w")
            f.write("httpcat")
            f.close()
            self.close()
        else:
            f = open("http.txt", "w")
            f.write("httpdog")
            f.close()
            self.close()
global url2
class myMainWindow(Ui_MainWindow,Ui_Window,Ui_set,QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()
        self.pv = 0
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(self.pv)
        self.progressBar.setRange(0, 4)
        self.pushButton.clicked.connect(self.get)
        self.action1.triggered.connect(self.action_save)
        self.action2.triggered.connect(self.action_to)


    def get(self):
        print("you push the button !")
        test1 = self.lineEdit.text()  #获取输入框中的code
        print("code is :",test1)
        self.progressBar.setValue(1)
        f = open("http.txt", "r")
        url = f.read()
        f.close()
        print("done !")
        print("a is :",url)
        global url2
        if url == ("httpcat") :
            url = ("https://http.cat/")
            url2 = url + test1
            print("will wget the jpg !")
            print("the url is ",url2)
            self.progressBar.setValue(2)
        else:
            url = ("https://http.dog/")
            text2 = ".jpg"
            url2 = url + test1 + text2
            print("will wget the jpg !")
            print("the url is ",url2)
            self.progressBar.setValue(2)
            os.remove("http.txt")
        import requests
        request = requests.get(url2)
        a = request.status_code
        if a == 200:
            self.progressBar.setValue(3)
            #wget.download(url2,"./lib/http_cat/lib/jpg/1.jpg")
            print("done !")             #获取图片
            content = requests.get(url2).content
            picture = QtGui.QImage.fromData(content)
            pixmap = QtGui.QPixmap.fromImage(picture)
            self.label_3.setPixmap(QPixmap(pixmap))
            self.label_3.setScaledContents(True)
            print("show the image done!")#显示图片
            self.progressBar.setValue(4)
        else:
            print("err! 404 Not Found!")
            self.label_3.setText("404 Not Found")
            self.progressBar.setValue(4)


    def action_save(self,):
        print("will save the jpg!")
        content = requests.get(url2).content
        test1 = self.lineEdit.text()
        name = test1 + ".jpg"
        with open(name, 'wb') as fp:
            fp.write(content)
        print("done!")
    def action_to(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "文件保存",
                                    self.cwd,  # 起始路径
                                    "图片文件 (*.jpg);;所有文件 (*)")

        if fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择要保存的文件为:")
        print(fileName_choose)
        print("文件筛选器类型: ", filetype)
        content = requests.get(url2).content
        with open(fileName_choose, 'wb') as fp:
            fp.write(content)
        #name = test1 + ".jpg"
        #shutil.copyfile(name,fileName_choose)
        print("copy done!")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()     #主窗口

    child = about_window()
    btn = vieo_gui.action4
    btn.triggered.connect(child.show)       #关于窗口

    set_1 = set_window()
    set = vieo_gui.action5
    set.triggered.connect(set_1.show)#设置窗口


    sys.exit(app.exec_())