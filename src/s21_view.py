from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QDoubleValidator
from s21_view_ui import Ui_View
from s21_view_graph import ViewGraph


class View(QMainWindow, Ui_View):

    equal_press_calc_signal = Signal(str, str)
    equal_press_graph_signal = Signal(str, str, str)

    def __init__(self, view_model, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._view_model = view_model
        self._exp_evaluated = False

        self.calcMode.toggled.connect(self.on_calc_mode_toggled)
        self.graphMode.toggled.connect(self.on_graph_mode_toggled)
        self.calcMode.setChecked(True)
        self.graphMode.setChecked(False)

        self._view_model.result_calculate_signal.connect(self.update_result)
        self._view_model.result_error_signal.connect(self.calculation_error)
        self._view_model.result_plot_graph_signal.connect(
            self.open_graph)
        self.equal_press_calc_signal.connect(
            self._view_model.calculate_expression)
        self.equal_press_graph_signal.connect(
            self._view_model.plot_graph)

        self.pushButton_equal.clicked.connect(self.on_equal_press)
        self.pushButton_0.clicked.connect(self.button_to_result)
        self.pushButton_1.clicked.connect(self.button_to_result)
        self.pushButton_2.clicked.connect(self.button_to_result)
        self.pushButton_3.clicked.connect(self.button_to_result)
        self.pushButton_4.clicked.connect(self.button_to_result)
        self.pushButton_5.clicked.connect(self.button_to_result)
        self.pushButton_6.clicked.connect(self.button_to_result)
        self.pushButton_7.clicked.connect(self.button_to_result)
        self.pushButton_8.clicked.connect(self.button_to_result)
        self.pushButton_9.clicked.connect(self.button_to_result)
        self.pushButton_cos.clicked.connect(self.button_to_result_with_bracket)
        self.pushButton_sin.clicked.connect(self.button_to_result_with_bracket)
        self.pushButton_tan.clicked.connect(self.button_to_result_with_bracket)
        self.pushButton_acos.clicked.connect(
            self.button_to_result_with_bracket)
        self.pushButton_asin.clicked.connect(
            self.button_to_result_with_bracket)
        self.pushButton_atan.clicked.connect(
            self.button_to_result_with_bracket)
        self.pushButton_mod.clicked.connect(self.button_to_result)
        self.pushButton_log.clicked.connect(self.button_to_result_with_bracket)
        self.pushButton_ln.clicked.connect(self.button_to_result_with_bracket)
        self.pushButton_close_bracket.clicked.connect(self.button_to_result)
        self.pushButton_open_bracket.clicked.connect(self.button_to_result)
        self.pushButton_div.clicked.connect(self.button_to_result)
        self.pushButton_mul.clicked.connect(self.button_to_result)
        self.pushButton_plus.clicked.connect(self.button_to_result)
        self.pushButton_minus.clicked.connect(self.button_to_result)
        self.pushButton_point.clicked.connect(self.button_to_result)
        self.pushButton_pow.clicked.connect(self.button_to_result)
        self.pushButton_sqrt.clicked.connect(
            self.button_to_result_with_bracket)
        self.pushButton_x.clicked.connect(self.button_to_result)
        self.pushButton_clear.clicked.connect(self.clear_result)

        x_validator = QDoubleValidator(
            float('-inf'), float('inf'),
            -1,
            self
        )
        x_validator.setNotation(QDoubleValidator.StandardNotation)

        self.valueX.setValidator(x_validator)
        self.valueXMax.setValidator(x_validator)
        self.valueXMin.setValidator(x_validator)

    @Slot()
    def button_to_result(self, with_bracket: bool = False):
        if self._exp_evaluated:
            self.clear_result()
            self._exp_evaluated = False

        button = self.sender()
        new_label = self.expressionText.text() + button.text() + \
            ("(" if with_bracket else "")
        self.expressionText.setText(new_label)

    @Slot()
    def button_to_result_with_bracket(self):
        self.button_to_result(True)

    def on_calc_mode_toggled(self, checked):
        self.calcX.setVisible(checked)

    def on_graph_mode_toggled(self, checked):
        self.graphX.setVisible(checked)

    def on_equal_press(self):
        if self.graphMode.isChecked():
            self.equal_press_graph_signal.emit(
                self.expressionText.text(), self.valueXMin.text(), self.valueXMax.text())
        else:
            self.equal_press_calc_signal.emit(
                self.expressionText.text(), self.valueX.text())
        self._exp_evaluated = True

    def update_result(self, result):
        self.expressionText.setText(f"{result:.17g}")

    def calculation_error(self, error: str):
        self.expressionText.setText(error)

    def open_graph(self, x, y):
        self._plot_window = ViewGraph(
            f"{self.expressionText.text()} ({self.valueXMin.text()} <= x <= {self.valueXMax.text()})")
        self._plot_window.plot_graph(x, y)
        self._plot_window.show()

    def clear_result(self):
        self.expressionText.setText('')
