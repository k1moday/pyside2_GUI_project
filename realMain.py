# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'realMain.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../../Desktop/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:white")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionget = QAction(MainWindow)
        self.actionget.setObjectName(u"actionget")
        self.actionedit = QAction(MainWindow)
        self.actionedit.setObjectName(u"actionedit")
        self.actiondelete = QAction(MainWindow)
        self.actiondelete.setObjectName(u"actiondelete")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 100, 411, 271))
        self.label.setPixmap(QPixmap(u"../../Desktop/src=http___dl.ppt123.net_pptbj_51_20181115_lcwgjs0t3d4.jpg&refer=http___dl.ppt123.jpg"))
        self.label.setScaledContents(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 430, 121, 51))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 430, 121, 51))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 430, 121, 51))
        self.pushButton_3.setStyleSheet(u"QPushButuon {\n"
"	background-color:rgb(249, 252, 255);\n"
"	border-radius:3px;\n"
"}\n"
"QPushBotton:hover{\n"
"	background-color:rgb(46, 182, 255)\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 170, 452, 141))
        self.label_2.setPixmap(QPixmap(u"../../Desktop/\u65e0\u6807\u9898.png"))
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actionnew)
        self.menu.addAction(self.actionsave)
        self.menu_2.addAction(self.actionget)
        self.menu_2.addAction(self.actionedit)
        self.menu_2.addAction(self.actiondelete)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u822a\u5929\u7535\u5b50\u4ea7\u54c1\u5bff\u547d\u68c0\u6d4b\u63a7\u5236\u5e73\u53f0", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionget.setText(QCoreApplication.translate("MainWindow", u"get", None))
        self.actionedit.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.actiondelete.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bff\u547d\u76d1\u6d4b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5bff\u547d\u63a7\u5236", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5bfc\u5165", None))
        self.label_2.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

