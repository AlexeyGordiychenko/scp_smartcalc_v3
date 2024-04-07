from PySide6.QtCore import QObject, Signal
import numpy as np


class ViewModel(QObject):
    # Signal to notify the View about changes in the ViewModel
    result_calculate_signal = Signal(float)
    result_error_signal = Signal(str)
    result_plot_graph_signal = Signal(list, list)

    def __init__(self, model):
        super().__init__()
        self._model = model

    def calculate(self, x):
        try:
            return self._model.calculate(x)
        except Exception as e:
            return np.nan

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
            self.result_calculate_signal.emit(self.calculate(x))
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
        step = 0.01 if abs(x_max-x_min) <= 10 else 0.1
        x = np.arange(x_min, x_max, step)
        y = [self.calculate(x) for x in x]
        self.result_plot_graph_signal.emit(x, y)
