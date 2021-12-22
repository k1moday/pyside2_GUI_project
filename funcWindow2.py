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




class Func2Window(QMainWindow):
    dictType = []
    flag = 0
    dictType2 = []
    flag2 = 0

    def __init__(self, parent=None):
        super(Func2Window, self).__init__(parent=parent)
        self.ui = QUiLoader().load('monitor2.ui')
        # self.ui.show()
        self.ui.tableWidget_5.clearContents()
        self.ui.pushButton_21.clicked.connect(self.saveall)
        self.ui.pushButton_20.clicked.connect(self.inputall)
        self.ui.pushButton_17.clicked.connect(self.ui.close)
        self.ui.pushButton_4.clicked.connect(self.ui.close)
        self.ui.pushButton_2.clicked.connect(self.addRow)
        self.ui.pushButton.clicked.connect(self.addRow2)

        self.ui.pushButton_6.clicked.connect(self.inputall2)
        self.ui.pushButton_7.clicked.connect(self.saveall2)

        fi = open("failure.txt", "r")
        data = fi.readlines()
        for index in range(len(data)):
            temp = data[index].split()
            if len(temp) == 0:
                break
            if not self.dictType.__contains__(temp[0]):
                self.dictType.append(temp[0])
            for indexi in range(len(temp)):
                self.ui.tableWidget_5.setItem(index, indexi, QTableWidgetItem(str(temp[indexi])))

        fi.close()

        fi = open("Component.txt")
        data = fi.readlines()
        for index in range(len(data)):
            temp = data[index].split()
            if len(temp) == 0:
                break
            if not self.dictType2.__contains__(temp[0]):
                self.dictType2.append(temp[0])
            for indexi in range(len(temp)):
                self.ui.tableWidget_2.setItem(index, indexi, QTableWidgetItem(str(temp[indexi])))
        fi.close()

        self.ui.comboBox_3.addItems(self.dictType)
        self.ui.comboBox.addItems(self.dictType2)
        self.ui.comboBox_3.currentIndexChanged.connect(self.handleSelectionChange)
        self.ui.comboBox.currentIndexChanged.connect(self.handleSelectionChange2)
        self.ui.pushButton_18.clicked.connect(self.restore)
        self.ui.pushButton_19.clicked.connect(self.delete)
        self.ui.pushButton_8.clicked.connect(self.restore2)
        self.ui.pushButton_9.clicked.connect(self.delete2)

        self.curSituationSave()

    def saveall(self):
        if self.flag == 1:
            QMessageBox.warning(self, '操作失败', '当前显示为筛选后的搜索结果，如需保存请点击撤销筛选')
            return
        fo = open("failiure.txt", "w")
        rowNum = self.ui.tableWidget_5.rowCount()
        columnNum = self.ui.tableWidget_5.columnCount()
        for i in range(0, rowNum):
            tempStr = ""
            for j in range(0, columnNum):
                temp = self.ui.tableWidget_5.item(i, j)
                if self.ui.tableWidget_5.item(i, j) is None:
                    break
                tempStr = tempStr + str(self.ui.tableWidget_5.item(i, j).text()) + " "
            fo.write(tempStr + "\n")
        fo.close()
        QMessageBox.information(self, '操作成功', '数据已保存到failiure.txt文件')

    def saveall2(self):
        if self.flag2 == 1:
            QMessageBox.warning(self, '操作失败', '当前显示为筛选后的搜索结果，如需保存请点击撤销筛选')
            return
        fo = open("Component.txt", "w")
        rowNum = self.ui.tableWidget_2.rowCount()
        columnNum = self.ui.tableWidget_2.columnCount()
        for i in range(0, rowNum):
            tempStr = ""
            for j in range(0, columnNum):
                temp = self.ui.tableWidget_2.item(i, j)
                if self.ui.tableWidget_2.item(i, j) is None:
                    break
                tempStr = tempStr + str(self.ui.tableWidget_2.item(i, j).text()) + " "
            fo.write(tempStr + "\n")
        fo.close()
        QMessageBox.information(self, '操作成功', '数据已保存到Component.txt文件')

    def curSituationSave(self):
        fo = open("tempFailiure.txt", "w")
        rowNum = self.ui.tableWidget_5.rowCount()
        columnNum = self.ui.tableWidget_5.columnCount()
        for i in range(0, rowNum):
            tempStr = ""
            for j in range(0, columnNum):
                temp = self.ui.tableWidget_5.item(i, j)
                if self.ui.tableWidget_5.item(i, j) is None:
                    break
                tempStr = tempStr + str(self.ui.tableWidget_5.item(i, j).text()) + " "
            fo.write(tempStr + "\n")
        fo.close()
        # QMessageBox.information(self, '操作成功', '数据已保存到Component.txt文件')

    def curSituationSave2(self):
        fo = open("tempComponent.txt", "w")
        rowNum = self.ui.tableWidget_2.rowCount()
        columnNum = self.ui.tableWidget_2.columnCount()
        for i in range(0, rowNum):
            tempStr = ""
            for j in range(0, columnNum):
                temp = self.ui.tableWidget_2.item(i, j)
                if self.ui.tableWidget_2.item(i, j) is None:
                    break
                tempStr = tempStr + str(self.ui.tableWidget_2.item(i, j).text()) + " "
            fo.write(tempStr + "\n")
        fo.close()
        # QMessageBox.information(self, '操作成功', '数据已保存到Component.txt文件')

    def inputall(self):
        path, _ = QFileDialog.getOpenFileName()
        fi = open(path, "r")
        data = fi.readlines()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            for indexj in range(len(temp)):
                self.ui.tableWidget_5.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()

    def inputall2(self):
        path, _ = QFileDialog.getOpenFileName()
        fi = open(path, "r")
        data = fi.readlines()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            for indexj in range(len(temp)):
                self.ui.tableWidget_2.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()

    def handleSelectionChange(self):
        curType = self.ui.comboBox_3.currentText()
        if self.flag == 0:
            self.curSituationSave()
        fi = open("tempFailiure.txt", "r")
        data = fi.readlines()
        curTypelist = []
        self.ui.tableWidget_5.clearContents()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            if len(temp) == 0:
                break
            if temp[0] == curType:
                curTypelist.append(temp)

        for indexi in range(len(curTypelist)):
            temp = curTypelist[indexi]
            for indexj in range(len(temp)):
                self.ui.tableWidget_5.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()
        self.flag = 1

    def handleSelectionChange2(self):
        curType = self.ui.comboBox.currentText()
        if self.flag2 == 0:
            self.curSituationSave2()
        fi = open("tempComponent.txt", "r")
        data = fi.readlines()
        curTypelist = []
        self.ui.tableWidget_2.clearContents()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            if len(temp) == 0:
                break
            if temp[0] == curType:
                curTypelist.append(temp)

        for indexi in range(len(curTypelist)):
            temp = curTypelist[indexi]
            for indexj in range(len(temp)):
                self.ui.tableWidget_2.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()
        self.flag2 = 1

    def restore(self):
        fi = open("tempFailiure.txt", "r")
        data = fi.readlines()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            for indexj in range(len(temp)):
                self.ui.tableWidget_5.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()
        self.flag = 0

    def restore2(self):
        fi = open("tempComponent.txt", "r")
        data = fi.readlines()
        for indexi in range(len(data)):
            temp = data[indexi].split()
            for indexj in range(len(temp)):
                self.ui.tableWidget_2.setItem(indexi, indexj, QTableWidgetItem(str(temp[indexj])))
        fi.close()
        self.flag2 = 0

    def delete(self):
        if self.flag == 1:
            QMessageBox.warning(self, '操作失败', '当前显示为筛选后的搜索结果，如需删除该数据请点击撤销筛选')
            return
        currentRow = self.ui.tableWidget_5.currentRow()
        self.ui.tableWidget_5.removeRow(currentRow)
        QMessageBox.information(self, '操作成功', '已删除该行，如需保存修改结果请点击导出按钮')
        self.curSituationSave()

    def delete2(self):
        if self.flag2 == 1:
            QMessageBox.warning(self, '操作失败', '当前显示为筛选后的搜索结果，如需删除该数据请点击撤销筛选')
            return
        currentRow = self.ui.tableWidget_2.currentRow()
        self.ui.tableWidget_2.removeRow(currentRow)
        QMessageBox.information(self, '操作成功', '已删除该行，如需保存修改结果请点击导出按钮')
        self.curSituationSave2()

    def addRow(self):
        rowNum = self.ui.tableWidget_5.rowCount()
        self.ui.tableWidget_5.insertRow(rowNum)

    def addRow2(self):
        rowNum = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(rowNum)
