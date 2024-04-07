import pyqtgraph as pg
from PySide6.QtWidgets import QVBoxLayout, QWidget


class ViewGraph(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self._plot_widget = pg.PlotWidget()
        layout.addWidget(self._plot_widget)
        self.setLayout(layout)

    def plot_graph(self, x, y):
        self._plot_widget.plot(x, y)
