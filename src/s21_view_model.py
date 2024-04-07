from PySide6.QtCore import QObject, Signal
import numpy as np


class ViewModel(QObject):
    # Signal to notify the View about changes in the ViewModel
    result_calculate_signal = Signal(float)
    result_error_signal = Signal(str)
    result_plot_graph_signal = Signal(list, list)

    def __init__(self, model, max_graph_range=1000000):
        super().__init__()
        self._model = model
        self._max_graph_range = max_graph_range

    def calculate(self, x, check_range=False):
        try:
            result = self._model.calculate(x)
            if check_range and abs(result) > self._max_graph_range:
                return np.nan
            return result
        except Exception as e:
            return np.nan

    def check_x_value(self, x):
        try:
            return True, float(x)
        except ValueError:
            return False, 0

    def calculate_expression(self, expression, x):
        x_exp = "x" in expression.lower()
        check, x = self.check_x_value(x)
        if x_exp and not check:
            self.result_error_signal.emit("Invalid 'x' value")
            return
        try:
            self._model.parse_expression(expression)
            self.result_calculate_signal.emit(self.calculate(x))
        except Exception as e:
            self.result_error_signal.emit(str(e))

    def plot_graph(self, expression, x_min, x_max):
        x_exp = "x" in expression.lower()
        check_min, x_min = self.check_x_value(x_min)
        check_max, x_max = self.check_x_value(x_max)
        if not x_exp:
            self.result_error_signal.emit("No 'x' in the expression")
            return
        elif not check_min or not check_max:
            self.result_error_signal.emit("Invalid 'x' value")
            return

        try:
            self._model.parse_expression(expression)
        except Exception as e:
            self.result_error_signal.emit(str(e))
            return

        if x_max > self._max_graph_range:
            x_max = self._max_graph_range
        if x_min < -self._max_graph_range:
            x_min = -self._max_graph_range
        step = 0.01 if abs(x_max-x_min) <= 10 else 0.1
        x = np.arange(x_min, x_max, step)
        y = [self.calculate(x, True) for x in x]
        self.result_plot_graph_signal.emit(x, y)
