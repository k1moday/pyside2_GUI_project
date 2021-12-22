import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from qt_material import apply_stylesheet
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader

from mainwindow import Ui_Dialog
from realMain import Ui_MainWindow
from funcWindow2 import Func2Window


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QMetaObject.connectSlotsByName(self)

        self.subWindow = Func1Window()
        self.subWindow2 = Func2Window()

        self.ui.pushButton_3.clicked.connect(self.subwindowshow2)
        self.ui.pushButton.clicked.connect(self.subwindowshow)
        print(QSqlDatabase.drivers())

    def subwindowshow(self):
        self.subWindow.ui.show()

    def subwindowshow2(self):
        self.subWindow2.ui.show()


class Func1Window(QMainWindow):
    def __init__(self, parent=None):
        super(Func1Window, self).__init__(parent=parent)
        self.ui = QUiLoader().load('monitor1.ui')
        # self.ui.show()
        self.ui.tableWidget.clearContents()
        self.ui.pushButton_2.clicked.connect(self.saveall)
        self.ui.pushButton.clicked.connect(self.inputall)
        self.ui.pushButton_3.clicked.connect(self.ui.close)

    def saveall(self):
        fo = open("foo.txt", "w")
        rowNum = self.ui.tableWidget.rowCount()
        columnNum = self.ui.tableWidget.columnCount()
        for i in range(0, rowNum):
            tempStr = ""
            for j in range(0, columnNum):
                temp = self.ui.tableWidget.item(i, j)
                if self.ui.tableWidget.item(i, j) is None:
                    break
                tempStr = tempStr + str(self.ui.tableWidget.item(i, j).text()) + " "
            fo.write(tempStr + "\n")
        fo.close()
        QMessageBox.information(self, '操作成功', '数据已保存到foo.txt文件')

    def inputall(self):
        path, _ = QFileDialog.getOpenFileName()
        fi = open(path, "r")
        data = fi.readlines()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            for indexj in range(len(temp)):
                self.ui.tableWidget.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
