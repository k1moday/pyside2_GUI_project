from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mainwindow import Ui_Dialog
from untitled import Ui_Form


class NewForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QApplication([])
mainw = NewForm()
mainw.show()
app.exec_()
