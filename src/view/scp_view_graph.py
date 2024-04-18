import pyqtgraph as pg
from PySide6.QtWidgets import QVBoxLayout, QWidget
import PySide6.QtCore as QtCore


class ViewGraph(QWidget):
    def __init__(self, title="Graph"):
        super().__init__()

        # To free the window on close, because we store refs to graph windows in
        # the View
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        # Add the widget
        layout = QVBoxLayout()
        self._plot_widget = pg.PlotWidget()
        layout.addWidget(self._plot_widget)
        self.setLayout(layout)
        # Set the window title
        self.setWindowTitle(title)

    def plot_graph(self, x, y):
        self._plot_widget.plot(x, y)
