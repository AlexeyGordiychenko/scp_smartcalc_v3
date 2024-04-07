from PySide6.QtCore import QObject, Signal
import numpy as np


class ViewModel(QObject):
    # Signal to notify the View about changes in the ViewModel
    result_calculate_signal = Signal(float)
    result_error_signal = Signal(str)
    result_plot_graph_start_signal = Signal()
    result_plot_graph_add_segment_signal = Signal(list, list)
    result_plot_graph_show_signal = Signal()

    def __init__(self, model):
        super().__init__()
        self._model = model

    def calculate_expression(self, expression, x):
        if "x" in expression.lower():
            try:
                x = float(x)
            except ValueError:
                self.result_error_signal.emit("Invalid 'x' value")
                return
        else:
            x = 0
        try:
            self._model.parse_expression(expression)
            self.result_calculate_signal.emit(self._model.calculate(x))
        except Exception as e:
            self.result_error_signal.emit(str(e))

    def plot_graph(self, expression, x_min, x_max):
        if "x" not in expression.lower():
            raise ValueError("No 'x' in the expression, can't plot a graph")
        else:
            try:
                x_min = float(x_min)
                x_max = float(x_max)
            except ValueError:
                self.result_error_signal.emit("Invalid 'x' value")
                return

        try:
            self._model.parse_expression(expression)
        except Exception as e:
            self.result_error_signal.emit(str(e))
            return

        self.result_plot_graph_start_signal.emit()
        x = np.linspace(x_min, x_max, 100)
        y = [self._model.calculate(x) for x in x]
        self.result_plot_graph_add_segment_signal.emit(x, y)
        self.result_plot_graph_show_signal.emit()
