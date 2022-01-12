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
        MainWindow.resize(820, 538)
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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setPixmap(QPixmap(u"../../Desktop/src=http___img-qn.51miz.com_preview_element_00_01_15_63_E-1156317-BD8B7258.jpg&refer=http___img-qn.51miz.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1 Light")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius: 8px;\n"
"	border-style:solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 182, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(16777215, 70))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 182, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(16777215, 70))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 182, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"QMenu {\n"
"     background-color : white;\n"
"     color :  black ;\n"
"}\n"
"QMenu::item:selected {\n"
"     background-color :  rgb(0, 170, 255);\n"
"     color :  black ;\n"
"}")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setStyleSheet(u"QMenu {\n"
"     background-color : white;\n"
"     color :  black ;\n"
"}\n"
"QMenu::item:selected {\n"
"     background-color :  rgb(0, 170, 255);\n"
"     color :  black ;\n"
"}")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setStyleSheet(u"QMenu {\n"
"     background-color : white;\n"
"     color :  black ;\n"
"}\n"
"QMenu::item:selected {\n"
"     background-color :  rgb(0, 170, 255);\n"
"     color :  black ;\n"
"}")
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
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5bff\u547d\u7279\u5f81\u76d1\u6d4b", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bff\u547d\u7279\u5f81\u68c0\u6d4b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5bff\u547d\u63a7\u5236", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

