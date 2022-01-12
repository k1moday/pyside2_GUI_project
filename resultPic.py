import matplotlib
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from myFigureCanvas import MyFigureCanvas2

matplotlib.use("Qt5Agg")


class ResultPic(QMainWindow):

    def __init__(self, parent=None):
        super(ResultPic, self).__init__(parent=parent)
        loader = QUiLoader()
        self.ui = loader.load("resultPic.ui")
        self.ui.pushButton.clicked.connect(self.ui.close)
        # self.graph_content_PR = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
        #                                        height=self.ui.graphicsView.height() / 101
        #                                        )
        self.graph_content_PR = MyFigureCanvas2()
        self.graphic_scene_PR = QGraphicsScene()

    def draw(self, xs, ys):
        y_pos = range(1, len(ys) + 1)
        self.graph_content_PR.axes.bar(xs, ys, align='center', alpha=0.7)
        # self.graph_content_PR.axes.set_title(title)
        self.graphic_scene_PR.addWidget(self.graph_content_PR)
        self.ui.graphicsView.setScene(self.graphic_scene_PR)
        self.ui.graphicsView.show()
