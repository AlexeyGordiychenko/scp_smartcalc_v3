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

        step = 0.01 if abs(x_max-x_min) <= 10 else 0.1
        x = np.arange(x_min, x_max, step)
        y = [self.calculate(x) for x in x]
        self.result_plot_graph_signal.emit(x, y)
