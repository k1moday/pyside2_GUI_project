# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelImport.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_modelImport(object):
    def setupUi(self, modelImport):
        if not modelImport.objectName():
            modelImport.setObjectName(u"modelImport")
        modelImport.resize(400, 300)
        self.pushButton = QPushButton(modelImport)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 40, 131, 51))
        self.pushButton_2 = QPushButton(modelImport)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 130, 131, 51))
        self.pushButton_3 = QPushButton(modelImport)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 240, 61, 21))

        self.retranslateUi(modelImport)

        QMetaObject.connectSlotsByName(modelImport)
    # setupUi

    def retranslateUi(self, modelImport):
        modelImport.setWindowTitle(QCoreApplication.translate("modelImport", u"\u6a21\u578b\u5bfc\u5165", None))
        self.pushButton.setText(QCoreApplication.translate("modelImport", u"\u5bfc\u5165\u7535\u8def\u7f51\u8868", None))
        self.pushButton_2.setText(QCoreApplication.translate("modelImport", u"\u5bfc\u5165\u6709\u9650\u5143\u5206\u6790\u8f93\u51fa", None))
        self.pushButton_3.setText(QCoreApplication.translate("modelImport", u"\u9000\u51fa", None))
    # retranslateUi

