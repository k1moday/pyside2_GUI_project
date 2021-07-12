from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mainwindow import Ui_Dialog
from untitled import Ui_Form
from realMain import Ui_MainWindow


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QMetaObject.connectSlotsByName(self)
        self.subWindow = Func1Window(parent=self)

        self.ui.pushButton.clicked.connect(self.subwindowshow)
        # @Slot()
        # def on_subwindow_clicked(self):
        # self.subWindow.show()

    def subwindowshow(self):
        self.subWindow.show()
        # self.subWindow.show()
    # self.pushButton.clicked(self.func)


class Func1Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Func1Window, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec_()
