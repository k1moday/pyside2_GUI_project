import sys
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from qt_material import apply_stylesheet
from PySide2.QtUiTools import QUiLoader

from funcWindow2 import Func2Window
from funcWindow1 import Func1Window


class MainWindow:
    def __init__(self):
        self.ui = QUiLoader().load('realMain.ui')

        self.subWindow = Func1Window()
        self.subWindow2 = Func2Window()

        self.ui.pushButton_3.clicked.connect(self.subwindowshow2)
        self.ui.pushButton.clicked.connect(self.subwindowshow)
        print(QSqlDatabase.drivers())

    def subwindowshow(self):
        self.subWindow.ui.show()

    def subwindowshow2(self):
        self.subWindow2.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    extra = {

        # Button colors
        'danger': '#dc3545',
        'warning': '#ffc107',
        'success': '#17a2b8',

        # Font
        'font-family': 'Microsoft YaHei',
    }
    apply_stylesheet(app, 'light_blue.xml', invert_secondary=True, extra=extra)
    mainWindow = MainWindow()
    mainWindow.ui.show()
    app.exec_()
