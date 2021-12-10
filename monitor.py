# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_monitor(object):
    def setupUi(self, monitor):
        if not monitor.objectName():
            monitor.setObjectName(u"monitor")
        monitor.resize(800, 600)
        self.pushButton = QPushButton(monitor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 40, 151, 31))
        self.pushButton_2 = QPushButton(monitor)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(620, 120, 151, 31))
        self.tableWidget = QTableWidget(monitor)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 40, 551, 501))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton_3 = QPushButton(monitor)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(650, 510, 101, 31))

        self.retranslateUi(monitor)

        QMetaObject.connectSlotsByName(monitor)
    # setupUi

    def retranslateUi(self, monitor):
        monitor.setWindowTitle(QCoreApplication.translate("monitor", u"\u5143\u5668\u4ef6\u5bff\u547d\u76d1\u6d4b", None))
        self.pushButton.setText(QCoreApplication.translate("monitor", u"\u67e5\u770b\u8be6\u7ec6\u4fe1\u606f", None))
        self.pushButton_2.setText(QCoreApplication.translate("monitor", u"\u5143\u5668\u4ef6\u5bff\u547d\u6a21\u578b\u56fe\u50cf\u663e\u793a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("monitor", u"\u5143\u5668\u4ef6\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("monitor", u"\u6e29\u5ea6", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("monitor", u"\u9884\u8ba1\u5bff\u547d", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("monitor", u"\u7535\u53c2\u6570", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("monitor", u"1", None));
        self.pushButton_3.setText(QCoreApplication.translate("monitor", u"\u9000\u51fa", None))
    # retranslateUi

