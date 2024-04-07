import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import QVBoxLayout, QWidget


class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

    def plot_graph(self, x, y):
        self.plot_widget.plot(x, y)
