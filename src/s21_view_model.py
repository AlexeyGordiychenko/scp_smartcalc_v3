from PySide6.QtCore import QObject, Signal


class ViewModel(QObject):
    # Signal to notify the View about changes in the ViewModel
    result_calculate_signal = Signal(float)
    result_error_signal = Signal(str)

    def __init__(self, model):
        super().__init__()
        self._model = model
        self._graph_mode = False
        self._calc_mode = True

    def calculate(self, expression, x_min, x_max):
        try:
            self._model.parse_expression(expression)
            self._expression = expression
            if self._graph_mode:
                pass
            elif self._calc_mode:
                self.calculate_expression(x_min)
        except Exception as e:
            self.result_error_signal.emit(str(e))

    def calculate_expression(self, x):
        if "x" in self._expression.lower():
            try:
                x = float(x)
            except ValueError:
                raise ValueError("Invalid 'x' value")
        else:
            x = 0
        self.result_calculate_signal.emit(self._model.calculate(x))

    def toggle_graph_mode(self, is_on):
        self._graph_mode = is_on

    def toggle_calc_mode(self, is_on):
        self._calc_mode = is_on
