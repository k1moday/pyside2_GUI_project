import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from qt_material import apply_stylesheet
from PySide2.QtWidgets import QFileDialog

from mainwindow import Ui_Dialog
from monitor import Ui_monitor
from realMain import Ui_MainWindow
from modelImport import Ui_modelImport
from monitor1 import Ui_monitor1
from graph import MainWindow2


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QMetaObject.connectSlotsByName(self)

        # self.subWindow2 = Func2Window(parent=self)

        self.subWindow = Func1Window(parent=self)
        self.subWindow2 = MainWindow2()
        # self.subWindow3 = func

        self.ui.pushButton.clicked.connect(self.subwindowshow2)
        self.ui.pushButton_3.clicked.connect(self.subwindowshow)
        # self.ui.pushButton_2.clicked.connect(self)
        print(QSqlDatabase.drivers())
        # @Slot()
        # def on_subwindow_clicked(self):
        # self.subWindow.show()

    # def subwindowshow2(self):
    #     self.subWindow2.show()

    def subwindowshow(self):
        self.subWindow.show()

    def subwindowshow2(self):
        self.subWindow2.show()

        # self.subWindow.show()
    # self.pushButton.clicked(self.func)


# class Func2Window(QMainWindow, Ui_monitor):
#     def __init__(self, parent=None):
#         super(Func2Window, self).__init__(parent=parent)
#         self.ui = Ui_monitor()
#         self.ui.setupUi(self)


class Func1Window(QMainWindow, Ui_monitor1):
    def __init__(self, parent=None):
        super(Func1Window, self).__init__(parent=parent)
        self.ui = Ui_monitor1()
        self.ui.setupUi(self)
        self.ui.tableWidget.clearContents()
        self.ui.pushButton_2.clicked.connect(self.saveall)
        self.ui.pushButton.clicked.connect(self.inputall)

    def saveall(self):
        fo = open("foo.txt", "w")
        rowNum = self.ui.tableWidget.rowCount()
        columnNum = self.ui.tableWidget.columnCount()
        for i in range(0, rowNum - 1):
            tempStr = ""
            for j in range(0, columnNum - 1):
                tempStr = tempStr + str(self.ui.tableWidget.item(i, j).text()) + " "
            fo.write(tempStr + "\n")
        fo.close()

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
    # apply_stylesheet(app, theme='dark_teal.xml')
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
