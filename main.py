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
from funcWindow1 import Func1Window


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
	apply_stylesheet(app, 'light_cyan_500.xml', invert_secondary=True, extra=extra)
	mainWindow = MainWindow()
	mainWindow.show()
	app.exec_()
