import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
# from qt_material import apply_stylesheet
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets
import pyqtgraph as pg
from PySide2.QtWidgets import QFileDialog
from netlist import netList


class Func1Window(QMainWindow):

	def __init__(self, parent=None):
		super(Func1Window, self).__init__(parent=parent)
		loader = QUiLoader()
		loader.registerCustomWidget(pg.PlotWidget)
		self.ui = loader.load("monitor1.ui")
		# self.ui = QUiLoader().load('monitor1.ui')
		# self.ui.show()
		self.ui.tableWidget.clearContents()
		self.ui.pushButton_2.clicked.connect(self.saveall)
		self.ui.pushButton.clicked.connect(self.inputall)
		self.ui.pushButton_3.clicked.connect(self.ui.close)
		self.ui.pushButton_5.clicked.connect(self.ui.close)
		self.ui.pushButton_7.clicked.connect(self.ui.close)
		self.ui.pushButton_4.clicked.connect(self.inputNet)
		self.ui.tableWidget_2.setRowCount(0)
		self.ui.pushButton_6.clicked.connect(self.inputGraph)
		self.ui.widget.setBackground('w')

	def saveall(self):
		fo = open("temperature.txt", "w")
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
		QMessageBox.information(self, '操作成功', '数据已保存到temperature.txt文件')

	def inputall(self):
		path, _ = QFileDialog.getOpenFileName()
		fi = open(path, "r")
		data = fi.readlines()
		for indexi in range(len(data)):
			temp = data[indexi].split()
			for indexj in range(len(temp)):
				self.ui.tableWidget.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
		fi.close()

	def inputNet(self):
		# path, _ = QFileDialog.getOpenFileName()
		# map = netList.buildNetList(path)
		# names = netList.getNames()
		names = [1, 2, 3]
		self.ui.tableWidget_2.setRowCount(0)
		self.ui.tableWidget_2.setRowCount(len(names))
		self.ui.tableWidget_2.setColumnCount(len(names))
		for index in range(len(names)):
			self.ui.tableWidget_2.setVerticalHeaderItem(index, QTableWidgetItem(str(names[index])))
			self.ui.tableWidget_2.setHorizontalHeaderItem(index, QTableWidgetItem(str(names[index])))

	# self.ui.tableWidget_2.setItem(0, 0, QTableWidgetItem("0"))

	def inputGraph(self):

		# 设置图表标题
		self.ui.widget.setTitle("电阻变化趋势", color='008080', size='12pt')

		# 设置上下左右的label
		self.ui.widget.setLabel("left", "V")
		self.ui.widget.setLabel("bottom", "s")
		# 背景色改为白色
		self.ui.widget.setBackground('w')
		# self.ui.horizontalLayout_9.addWidget(pw)

		path, _ = QFileDialog.getOpenFileName()
		fi = open(path, "r")
		xs = []
		ys = []
		data = fi.readlines()
		del data[0]
		for line in data:
			line = line.strip('\n')
			temp = line.split()
			xs.append(float(temp[0]))
			ys.append(float(temp[1]))
		fi.close()
		self.ui.widget.plot(xs,
		                    ys,
		                    pen=pg.mkPen('b')  # 线条颜色
		                    )
# print(path)
