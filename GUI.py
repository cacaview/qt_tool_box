# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(534, 431)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 50, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 50, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 130, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 130, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 130, 111, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 210, 111, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "xxx工具箱"))
        self.pushButton.setText(_translate("mainWindow", "短视频去水印下载"))
        self.pushButton_2.setText(_translate("mainWindow", "epub阅读器"))
        self.pushButton_3.setText(_translate("mainWindow", "快速分享文本"))
        self.pushButton_4.setText(_translate("mainWindow", "格式互转"))
        self.pushButton_5.setText(_translate("mainWindow", "新番放送"))
        self.pushButton_6.setText(_translate("mainWindow", "b站 BV/AV互转"))
        self.pushButton_7.setText(_translate("mainWindow", "谷歌翻译"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "常用工具"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "影音工具"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "图片工具"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("mainWindow", "游戏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("mainWindow", "其他工具"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("mainWindow", "开发工具"))
