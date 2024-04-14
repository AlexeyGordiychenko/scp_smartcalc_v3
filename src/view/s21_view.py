from datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Signal, Slot, QSettings
from PySide6.QtGui import QDoubleValidator, QColor
from .s21_view_ui import Ui_View
from .s21_view_graph import ViewGraph
import configparser


class View(QMainWindow, Ui_View):

    equal_press_calc_signal = Signal(str, str)
    equal_press_graph_signal = Signal(str, str, str)
    calculate_credit_signal = Signal(bool, str, str, str)

    def __init__(self, view_model, current_dir, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._view_model = view_model
        self._exp_evaluated = False
        self._plot_windows = []
        self._settings = QSettings("s21_APP2", "SmartCalc_v3")
        self._current_dir = current_dir

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

        self.credit_annuity.setChecked(True)
        self.credit_differentiated.setChecked(False)

        credit_validator = QDoubleValidator(0, float('inf'), 2, self)
        credit_validator.setNotation(QDoubleValidator.StandardNotation)
        self.credit_principal.setValidator(credit_validator)
        self.credit_rate.setValidator(credit_validator)
        self.credit_term.setValidator(credit_validator)

        self.credit_calc.clicked.connect(self.calculate_credit)
        self.calculate_credit_signal.connect(self._view_model.calculate_credit)
        self._view_model.result_calculate_credit_signal.connect(
            self.update_credit)
        self._view_model.result_error_credit_signal.connect(self.credit_error)

        self.historyRestore.clicked.connect(self.restore_expression)
        self.historyClear.clicked.connect(self.clear_history)
        self.historyList.itemDoubleClicked.connect(self.restore_expression)

        self.restore_settings()

        current_style = self.centralwidget.styleSheet()
        config = configparser.ConfigParser()
        config.read(os.path.join(self._current_dir, 'config.ini'))
        if 'Color' in config:
            bg_color = config.get('Color', 'background', fallback=None)
            if bg_color and QColor(bg_color).isValid():
                self.setStyleSheet(f"\nbackground-color: {bg_color};")
        if 'Font size' in config:
            btn_font_size = self.safe_config_getint(
                config, 'Font size', 'button')
            if btn_font_size:
                current_style += f"\nQPushButton {{font-size: {btn_font_size}pt;}}"
            tab_font_size = self.safe_config_getint(
                config, 'Font size', 'tab')
            if tab_font_size:
                current_style += f"\nQTabBar {{font-size: {tab_font_size}pt;}}"
            label_font_size = self.safe_config_getint(config,
                                                      'Font size', 'label')
            if label_font_size:
                current_style += f"\nQLabel {{font-size: {label_font_size}pt;}}"
            radio_font_size = self.safe_config_getint(config,
                                                      'Font size', 'radio')
            if radio_font_size:
                current_style += f"\nQRadioButton {{font-size: {radio_font_size}pt;}}"
        self.centralwidget.setStyleSheet(current_style)

        if 'Settings' in config:
            default_tab = self.safe_config_getint(config,
                                                  'Settings', 'default_tab', fallback=1)
            if default_tab and 1 <= default_tab <= 4:
                self.tabWidget.setCurrentIndex(default_tab - 1)

        logging_period = None
        if 'Logging' in config:
            logging_period = config.get('Logging', 'period')
        self.configure_logging(logging_period)

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
        if self._exp_evaluated:
            return
        self.historyList.insertItem(0, self.expressionText.text())
        logging.info('Operation performed: %s', self.expressionText.text())
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
        plot_window = ViewGraph(
            f"{self.expressionText.text()} ({self.valueXMin.text()} <= x <= {self.valueXMax.text()})")
        plot_window.plot_graph(x, y)
        plot_window.show()
        plot_window.destroyed.connect(
            lambda: self.remove_plot_window(plot_window))
        self._plot_windows.append(plot_window)

    def clear_result(self):
        self.expressionText.setText('')

    def closeEvent(self, event):
        for plot_window in self._plot_windows:
            plot_window.close()
        self._plot_windows.clear()
        self.save_settings()
        super().closeEvent(event)

    def remove_plot_window(self, window):
        if window in self._plot_windows:
            self._plot_windows.remove(window)

    def calculate_credit(self):
        self.calculate_credit_signal.emit(
            self.credit_annuity.isChecked(),
            self.credit_principal.text(),
            self.credit_term.text(),
            self.credit_rate.text())

    def update_credit(self, monthly_start, monthly_end, over, total):
        credit_monthly_text = f"{monthly_start:.2f}"
        if monthly_start != monthly_end:
            credit_monthly_text += f"...{monthly_end: .2f}"
        self.credit_monthly.setText(credit_monthly_text)
        self.credit_over.setText(f"{over:.2f}")
        self.credit_total.setText(f"{total:.2f}")

    def credit_error(self, err="Invalid input"):
        self.credit_monthly.setText(err)
        self.credit_over.setText(err)
        self.credit_total.setText(err)

    def restore_expression(self):
        current_expression = self.historyList.currentItem()
        if current_expression:
            self.expressionText.setText(current_expression.text())
            self.tabWidget.setCurrentIndex(0)

    def clear_history(self):
        if self.historyList.count() > 0:
            confirmation = QMessageBox.question(
                self,
                "Confirm history clean up", "Are you sure you want to clear the history?",
                QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                self.historyList.clear()

    def save_settings(self):
        self._settings.beginWriteArray("history")
        for i in range(self.historyList.count()):
            self._settings.setArrayIndex(i)
            self._settings.setValue(
                "expression", self.historyList.item(i).text())
        self._settings.endArray()

    def restore_settings(self):
        size = self._settings.beginReadArray("history")
        for i in range(size):
            self._settings.setArrayIndex(i)
            value = self._settings.value("expression")
            if value is not None:
                self.historyList.addItem(value)
        self._settings.endArray()

    def safe_config_getint(self, config, section, option, fallback=None):
        try:
            return config.getint(section, option, fallback=fallback)
        except ValueError:
            return fallback

    def configure_logging(self, logging_period):
        log_dir = os.path.join(self._current_dir, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(format=log_format, level=logging.INFO, handlers=[])

        interval = 1
        if logging_period == 'hour':
            rotation_period = 'H'
        elif logging_period == 'month':
            rotation_period = 'D'
            interval = 30
        else:
            rotation_period = 'D'

        log_file_name = os.path.join(log_dir, 'logs_{}.log'.format(
            datetime.now().strftime('%d-%m-%y-%H-%M-%S')))
        file_handler = TimedRotatingFileHandler(
            log_file_name, when=rotation_period, interval=interval)
        file_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(file_handler)