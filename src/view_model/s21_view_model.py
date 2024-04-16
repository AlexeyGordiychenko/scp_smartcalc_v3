from PySide6.QtCore import QObject, Signal
import numpy as np


class ViewModel(QObject):
    # Signals to notify the View
    calc_exp_signal = Signal(float)
    exp_error_signal = Signal(str)
    plot_graph_signal = Signal(list, list)
    calc_credit_signal = Signal(float, float, float, float)
    credit_error_signal = Signal()

    def __init__(self, model, max_graph_range=1000000):
        super().__init__()
        self._model = model
        self._max_graph_range = max_graph_range

    def plot_point_calculate(self, x):
        try:
            result = self._model.calculate(x)
            if abs(result) > self._max_graph_range:
                return np.nan
            return result
        except Exception as e:
            return np.nan

    def check_input_value(self, input):
        try:
            return True, float(input)
        except ValueError:
            return False, 0

    def calculate_expression(self, expression, x):
        x_exp = "x" in expression.lower()
        check, x = self.check_input_value(x)
        if x_exp and not check:
            self.exp_error_signal.emit("Invalid 'x' value")
            return
        try:
            self._model.parse_expression(expression)
            self.calc_exp_signal.emit(self._model.calculate(x))
        except Exception as e:
            self.exp_error_signal.emit(str(e))

    def plot_graph(self, expression, x_min, x_max):
        x_exp = "x" in expression.lower()
        check_min, x_min = self.check_input_value(x_min)
        check_max, x_max = self.check_input_value(x_max)
        if not x_exp:
            self.exp_error_signal.emit("No 'x' in the expression")
            return
        elif not check_min or not check_max or x_max < x_min:
            self.exp_error_signal.emit("Invalid 'x' value")
            return

        try:
            self._model.parse_expression(expression)
        except Exception as e:
            self.exp_error_signal.emit(str(e))
            return

        if x_max > self._max_graph_range:
            x_max = self._max_graph_range
        if x_min < -self._max_graph_range:
            x_min = -self._max_graph_range
        step = 0.01 if abs(x_max-x_min) <= 10 else 0.1
        x = np.arange(x_min, x_max, step)
        y = [self.plot_point_calculate(x) for x in x]
        self.plot_graph_signal.emit(x, y)

    def calculate_credit(self, is_annuity, principal, term, interest_rate):
        check_principal, principal = self.check_input_value(principal)
        check_term, term = self.check_input_value(term)
        check_interest_rate, interest_rate = self.check_input_value(
            interest_rate)
        if not check_principal or not check_term or not check_interest_rate:
            self.credit_error_signal.emit()
            return
        if is_annuity:
            res = self._model.credit_annuity(principal, term, interest_rate)
        else:
            res = self._model.credit_differentiated(
                principal, term, interest_rate)
        self.calc_credit_signal.emit(
            res.monthly_start, res.monthly_end, res.over, res.total)
