import shutil
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QFileDialog,QProgressBar)
import sys
import wget
from GUI_set import *
from GUI import *
import os
from GUI_about import *

url2 = 200
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
            f = open("./lib/http_cat/lib/http.txt", "w")
            f.write("httpcat")
            f.close()
            set_1.close()
        else:
            f = open("./lib/http_cat/lib/http.txt", "w")
            f.write("httpdog")
            f.close()
            set_1.close()


class myMainWindow(Ui_MainWindow,QMainWindow):
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
        #self.action3.triggered.connect(self.action_new)

    def get(self):
        print("you push the button !")
        test1 = self.lineEdit.text()    #获取输入框中的code
        print("code is :",test1)
        self.progressBar.setValue(1)
        f = open("./lib/http_cat/lib/http.txt", "r")
        url = f.read()
        print("done !")

        print("a is :",url)
        if url == ("httpcat") :
            url = ("https://http.cat/")
            url2: str = url + test1
            print("will wget the jpg !")
            print("the url is ",url2)
            self.progressBar.setValue(2)
        else:
            url = ("https://http.dog/")
            text2 = ".jpg"
            url2: str = url + test1 + text2
            print("will wget the jpg !")
            print("the url is ",url2)
            self.progressBar.setValue(2)
        import requests
        requests = requests.get(url2)
        a = requests.status_code
        if a == 200:
            if os.path.exists("./lib/http_cat/lib/jpg/1.jpg"):
                os.remove("./lib/http_cat/lib/jpg/1.jpg")
                print("remove the file")
                self.progressBar.setValue(3)
            else:
                print("The file does not exist")
                self.progressBar.setValue(3)
            wget.download(url2,"./lib/http_cat/lib/jpg/1.jpg")
            print("done !")             #获取图片
            self.label_3.setPixmap(QPixmap("./lib/http_cat/lib/jpg/1.jpg"))
            self.label_3.setScaledContents(True)
            print("show the image done!")#显示图片
            self.progressBar.setValue(4)
        else:
            print("err! 404 Not Found!")
            self.label_3.setText("404 Not Found")
            self.progressBar.setValue(4)


    def action_save(self,):
        print("will save the jpg!")
        if os.path.exists("./lib/http_cat/lib/jpg/1.jpg"):
            shutil.copyfile('./lib/http_cat/lib/jpg/1.jpg', './lib/http_cat/download/1.jpg')
            #wget.download(url2, "./download/1.jpg")
            print("copy done!")
            reply = QMessageBox.information(self, "成功", "已保存到本程序路径下的download目录",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)
        else:
            print("The file does not exist")
            reply = QMessageBox.warning(self, "警告", "找不到文件，尝试再次get图片", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            print(reply)
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
        shutil.copyfile('./lib/http_cat/lib/jpg/1.jpg',fileName_choose)
        print("copy done!")

    #def action_new(self):
        #os.system("start .\main.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()     #主窗口

    child = about_window()
    btn=vieo_gui.action4
    btn.triggered.connect(child.show)       #关于窗口

    set_1 = set_window()
    set=vieo_gui.action5
    set.triggered.connect(set_1.show)#设置窗口


    sys.exit(app.exec_())