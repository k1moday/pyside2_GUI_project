# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1024, 768)
        self.elecmodel = QTableWidget(Dialog)
        if (self.elecmodel.columnCount() < 3):
            self.elecmodel.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.elecmodel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.elecmodel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.elecmodel.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.elecmodel.setObjectName("elecmodel")
        self.elecmodel.setEnabled(True)
        self.elecmodel.setGeometry(QRect(70, 120, 531, 451))
        self.elecmodel.horizontalHeader().setProperty("showSortIndicator", False)
        self.elecmodel.horizontalHeader().setStretchLastSection(False)
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QRect(670, 460, 271, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(670, 380, 271, 61))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(670, 220, 271, 61))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(670, 140, 271, 61))
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QRect(670, 300, 271, 61))
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.elecmodel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u5df2\u5bfc\u5165\u7535\u8def\u6a21\u578b", None));
        ___qtablewidgetitem1 = self.elecmodel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u53c2\u6570", None));
        ___qtablewidgetitem2 = self.elecmodel.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u8f93\u51fa\u53c2\u6570", None));
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u90e8\u4ef6\u7ea7\u5bff\u547d\u91cf\u5316", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a\u5404\u7535\u8def\u5173\u7cfb", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6709\u9650\u5143\u5206\u6790\u53c2\u6570", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u4eff\u771f\u7535\u8def", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u7535\u8def\u7ea7\u5bff\u547d\u91cf\u5316", None))
    # retranslateUi

