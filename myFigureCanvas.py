import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")  # 声明使用QT5


class MyFigureCanvas(FigureCanvas):
    """
    通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    """

    def __init__(self, parent=None, width=5.5, height=5.5, dpi=100):
        # 创建一个Figure
        self.fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白

        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)

        self.axes = self.fig.add_subplot(111)  # 添加子图
        self.axes.spines['top'].set_visible(False)  # 去掉绘图时上面的横线
        self.axes.spines['right'].set_visible(False)  # 去掉绘图时右面的横线


class MyFigureCanvas2(FigureCanvas):
    """
    通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    """

    def __init__(self, parent=None, width=13, height=5, dpi=100):
        # 创建一个Figure
        self.fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白

        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)

        self.axes = self.fig.add_subplot(111)  # 添加子图
        self.axes.spines['top'].set_visible(False)  # 去掉绘图时上面的横线
        self.axes.spines['right'].set_visible(False)  # 去掉绘图时右面的横线