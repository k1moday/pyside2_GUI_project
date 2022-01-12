import matplotlib
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg
from PySide2.QtWidgets import QFileDialog
from netlist import NetList
from netImportance import Graph
from combine_FT import FTToimportance
from netList2topo import netList2Topo
from myFigureCanvas import MyFigureCanvas
from resultPic import ResultPic

matplotlib.use("Qt5Agg")


class Func1Window(QMainWindow):
    xs = []
    ys = []
    names = []
    xs2 = []
    ys2 = []

    def __init__(self, parent=None):
        super(Func1Window, self).__init__(parent=parent)
        loader = QUiLoader()
        loader.registerCustomWidget(pg.PlotWidget)
        # loader.registerCustomWidget(MplWidget)
        self.ui = loader.load("monitor1.ui")
        self.ui.tableWidget.clearContents()
        self.ui.pushButton_2.clicked.connect(self.saveall)
        self.ui.pushButton.clicked.connect(self.inputall)
        self.ui.pushButton_3.clicked.connect(self.ui.close)
        self.ui.pushButton_5.clicked.connect(self.ui.close)
        self.ui.pushButton_7.clicked.connect(self.ui.close)
        self.ui.pushButton_9.clicked.connect(self.ui.close)
        self.ui.pushButton_4.clicked.connect(self.inputNet)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.pushButton_6.clicked.connect(self.inputGraph)
        self.ui.pushButton_8.clicked.connect(self.inputMatrix)
        self.ui.pushButton_10.clicked.connect(self.computeMatrix)
        self.ui.pushButton_11.clicked.connect(self.resultPicShow)
        self.ui.pushButton_12.clicked.connect(self.resultPicShow2)
        self.ui.widget.setBackground('w')
        self.curMatrix = []
        self.subWindow = ResultPic()
        # self.graph_content_PR = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
        #                                        height=self.ui.graphicsView.height() / 101
        #                                        )
        self.graph_content_PR = MyFigureCanvas()
        self.graphic_scene_PR = QGraphicsScene()

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
        self.ui.tableWidget.resizeColumnsToContents()

    def inputNet(self):
        theNet = NetList()
        theNet.makeNetMap()
        names = theNet.getNames()
        netMap = theNet.getNetMap()
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_2.setRowCount(len(names))
        self.ui.tableWidget_2.setColumnCount(len(names))
        self.ui.tableWidget_3.setRowCount(1)
        self.ui.tableWidget_3.setColumnCount(len(names))
        topo = netList2Topo(netMap, names)
        self.graph_content_PR.axes.clear()
        nx.draw(topo, with_labels=True, ax=self.graph_content_PR.axes)
        self.graphic_scene_PR.addWidget(
            self.graph_content_PR)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.graphicsView.setScene(self.graphic_scene_PR)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()

        theGraph = Graph()
        edges_list = []
        for index in range(len(names)):
            self.ui.tableWidget_2.setVerticalHeaderItem(index, QTableWidgetItem(str(names[index])))
            self.ui.tableWidget_2.setHorizontalHeaderItem(index, QTableWidgetItem(str(names[index])))
        for indexi in range(len(netMap)):
            for indexj in range(len(netMap[0])):
                self.ui.tableWidget_2.setItem(indexi, indexj, QTableWidgetItem(str(netMap[indexi][indexj])))
                if netMap[indexi][indexj] == 1:
                    edges_list.append((names[indexi], names[indexj]))

        theGraph.add_edges(edges_list)
        rank = theGraph.pagerank()
        # print(rank)
        sortedRank = sorted(rank.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        # print(sorted(rank.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
        # print(sortedRank)
        self.xs = []
        self.ys = []
        for index in range(len(sortedRank)):
            self.ui.tableWidget_3.setHorizontalHeaderItem(index, QTableWidgetItem(str(sortedRank[index][0])))
            self.ui.tableWidget_3.setItem(0, index, QTableWidgetItem(str(round(sortedRank[index][1], 4))))
            self.xs.append(str(sortedRank[index][0]))
            self.ys.append(round(sortedRank[index][1], 4))
        self.ui.tableWidget_3.setVerticalHeaderItem(0, QTableWidgetItem('节点网络重要度'))
        # self.xs =
        self.ui.tableWidget_3.resizeColumnsToContents()

    # self.ui.tableWidget_2.setItem(0, 0, QTableWidgetItem("0"))

    def inputGraph(self):
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
        # 设置图表标题
        title = self.ui.lineEdit_2.text()
        self.ui.widget.setTitle(title, color='008080', size='12pt')
        leftStr = self.ui.lineEdit_3.text()
        bottomStr = self.ui.lineEdit_4.text()

        cut = ys[len(ys) - 200:len(ys):1]
        yMean = np.mean(cut)
        yVar = np.var(cut)
        self.ui.lineEdit_8.setText(str(max(cut)))
        self.ui.lineEdit_7.setText(str(min(cut)))
        self.ui.lineEdit_5.setText(str(round(yMean, 4)))
        self.ui.lineEdit_6.setText(str(round(yVar, 4)))

        # 设置上下左右的label
        self.ui.widget.setLabel("left", leftStr)
        self.ui.widget.setLabel("bottom", bottomStr)
        # 背景色改为白色
        self.ui.widget.setBackground('w')
        # self.ui.horizontalLayout_9.addWidget(pw)
        self.ui.widget.plot(xs,
                            ys,
                            pen=pg.mkPen('b')  # 线条颜色
                            )

    def inputMatrix(self):
        path, _ = QFileDialog.getOpenFileName()
        fi = open(path, "r")
        data = fi.readlines()
        fi.close()
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_6.setRowCount(0)
        matrix = []
        counter = 0
        index1 = 0
        for line in data:
            line = line.strip('\n')
            temp = line.split()
            tempVec = []
            self.names.append(temp[0])
            index1 = index1 + 1
            tempVec.append(str(index1))
            for index in range(1, len(temp)):
                tempVec.append(temp[index])
            if counter == 0:
                counter = len(temp)
            if counter != len(temp):
                QMessageBox.warning(self, '输入错误', '输入矩阵行向量长度不一致')
                return
            matrix.append(tempVec)

        theMatrix = np.zeros((len(matrix), len(matrix[0])), dtype=int)
        for indexi in range(len(matrix)):
            for indexj in range(len(matrix[0])):
                theMatrix[indexi][indexj] = int(matrix[indexi][indexj])

        self.ui.tableWidget_4.setRowCount(len(matrix))
        self.ui.tableWidget_4.setColumnCount(len(matrix[0]))
        self.ui.tableWidget_4.setHorizontalHeaderItem(0, QTableWidgetItem('节点名'))
        self.ui.tableWidget_4.setHorizontalHeaderItem(1, QTableWidgetItem('连接节点数'))
        self.ui.tableWidget_4.setHorizontalHeaderItem(2, QTableWidgetItem('连接逻辑'))
        self.ui.tableWidget_4.setHorizontalHeaderItem(3, QTableWidgetItem('后续为连接的节点名'))
        for index in range(4, len(matrix)):
            self.ui.tableWidget_4.setHorizontalHeaderItem(index, QTableWidgetItem(''))
        self.ui.tableWidget_4.resizeColumnsToContents()

        for index in range(len(matrix)):
            self.ui.tableWidget_4.setItem(index, 0, QTableWidgetItem(str(self.names[index])))
        for indexi in range(len(matrix)):
            for indexj in range(1, len(matrix[0])):
                self.ui.tableWidget_4.setItem(indexi, indexj, QTableWidgetItem(str(matrix[indexi][indexj])))

        matrixRun = FTToimportance()
        baseEvents = matrixRun.getBaseEvents(theMatrix)

        self.ui.tableWidget_6.setRowCount(1)
        self.ui.tableWidget_6.setColumnCount(len(baseEvents))
        for index in range(len(baseEvents)):
            self.ui.tableWidget_6.setHorizontalHeaderItem(index,
                                                          QTableWidgetItem(str(self.names[baseEvents[index] - 1])))
        self.ui.tableWidget_6.setVerticalHeaderItem(0, QTableWidgetItem('指数分布参数'))

        self.curMatrix = theMatrix

    def computeMatrix(self):
        if len(self.curMatrix) == 0:
            QMessageBox.warning(self, '输入错误', '请正确录入故障树矩阵')

        matrixRun = FTToimportance()
        baseEvents = matrixRun.getBaseEvents(self.curMatrix)
        lam = []
        for index in range(len(baseEvents)):
            if self.ui.tableWidget_6.item(0, index) is None:
                QMessageBox.warning(self, '输入错误', '请完整输入参数向量')
                return
            lam.append(float(self.ui.tableWidget_6.item(0, index).text()))
        trial = int(self.ui.lineEdit.text())
        if trial == '':
            QMessageBox.warning(self, '输入错误', '请输入训练次数')
            return

        nodeImportance = matrixRun.getImportance(self.curMatrix, trial, lam, baseEvents)
        self.ui.tableWidget_5.setRowCount(1)
        self.ui.tableWidget_5.setColumnCount(len(baseEvents))
        self.xs2 = []
        self.ys2 = []
        for index in range(len(baseEvents)):
            self.ui.tableWidget_5.setHorizontalHeaderItem(index,
                                                          QTableWidgetItem(str(self.names[baseEvents[index] - 1])))
            self.xs2.append(self.names[baseEvents[index] - 1])
            self.ui.tableWidget_5.setItem(0, index, QTableWidgetItem(str(nodeImportance[index])))
            self.ys2.append(nodeImportance[index])
        self.ui.tableWidget_5.resizeColumnsToContents()

    def resultPicShow(self):
        if self.xs is not [] and self.ys is not []:
            self.subWindow.draw(self.xs, self.ys)
            self.subWindow.ui.show()
        else:
            QMessageBox.warning(self, '导入错误', '请先导入网表模型')
            return

    def resultPicShow2(self):
        if self.xs2 is not [] and self.ys2 is not []:
            self.subWindow.draw(self.xs2, self.ys2)
            self.subWindow.ui.show()
        else:
            QMessageBox.warning(self, '逻辑错误', '请先进行前置计算')
            return
