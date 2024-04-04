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

    def calculate(self, expression):
        try:
            self._model.parse_expression(expression)
            self.result_calculate_signal.emit(self._model.calculate())
        except Exception as e:
            self.result_error_signal.emit(str(e))

    def toggle_graph_mode(self, is_on):
        self._graph_mode = is_on

    def toggle_calc_mode(self, is_on):
        self._calc_mode = is_on
