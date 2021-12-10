from PySide2 import QtWidgets
import pyqtgraph as pg
from PySide2.QtWidgets import QFileDialog


class MainWindow2(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('电仿真曲线')

        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()

        # 设置图表标题
        self.pw.setTitle("电阻变化趋势", color='008080', size='12pt')

        # 设置上下左右的label
        self.pw.setLabel("left", "V")
        self.pw.setLabel("bottom", "s")
        # 背景色改为白色
        self.pw.setBackground('w')
        # self.pw.setXRange(min=0,
        #                   max=0.01)

        # 创建其他Qt控件
        okButton = QtWidgets.QPushButton("OK")
        lineEdit = QtWidgets.QLineEdit('点击信息')
        # 水平layout里面放 edit 和 button
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(okButton)
        okButton.clicked.connect(self.openbox)

        # 垂直layout里面放 pyqtgraph图表控件 和 前面的水平layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.pw)
        vbox.addLayout(hbox)

        # 设置全局layout
        self.setLayout(vbox)

    def openbox(self):
        self.pw.clear()
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        path, _ = dialog.getOpenFileName()
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
        # hour 和 temperature 分别是 : x, y 轴上的值
        self.pw.plot(xs,
                     ys,
                     pen=pg.mkPen('b')  # 线条颜色
                     )
        # print(path)
