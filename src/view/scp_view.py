import logging.handlers
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Signal, Slot, QSettings, QLocale
from PySide6.QtGui import QDoubleValidator, QColor
from .scp_view_ui import Ui_View
from .scp_view_graph import ViewGraph
from datetime import datetime
import configparser
import logging
import os


class View(QMainWindow, Ui_View):

    calc_exp_signal = Signal(str, str)
    plot_graph_signal = Signal(str, str, str)
    calc_credit_signal = Signal(bool, str, str, str)

    def __init__(self, view_model, current_dir, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._view_model = view_model
        self._exp_evaluated = False
        self._mode_switched = False
        self._plot_windows = []
        self._settings = QSettings("scp_APP2", "SmartCalc_v3")
        self._current_dir = current_dir
        self._logging_period = None

        self.set_initial_ui()
        self.set_view_model_signals()
        self.set_ui_elements_signals()
        self.set_validators()
        self.restore_settings()
        self.parse_config()
        self.configure_logging()

    def set_initial_ui(self):
        self.tgl_calc.setChecked(True)
        self.tgl_graph.setChecked(False)
        self.credit_annuity.setChecked(True)
        self.credit_differentiated.setChecked(False)

    def set_view_model_signals(self):
        # From the view model
        self._view_model.calc_exp_signal.connect(self.update_result)
        self._view_model.exp_error_signal.connect(self.calculation_error)
        self._view_model.plot_graph_signal.connect(self.open_graph)
        self._view_model.calc_credit_signal.connect(self.update_credit)
        self._view_model.credit_error_signal.connect(self.credit_error)
        # To the view model
        self.calc_exp_signal.connect(self._view_model.calculate_expression)
        self.plot_graph_signal.connect(self._view_model.plot_graph)
        self.calc_credit_signal.connect(self._view_model.calculate_credit)

    def set_ui_elements_signals(self):
        # Calc buttons
        self.btn_equal.clicked.connect(self.evaluate_exp)
        self.expressionText.returnPressed.connect(self.evaluate_exp)
        self.expressionText.textChanged.connect(self.exp_text_changed)
        self.btn_clear.clicked.connect(self.clear_result)
        self.btn_0.clicked.connect(self.button_to_exp)
        self.btn_1.clicked.connect(self.button_to_exp)
        self.btn_2.clicked.connect(self.button_to_exp)
        self.btn_3.clicked.connect(self.button_to_exp)
        self.btn_4.clicked.connect(self.button_to_exp)
        self.btn_5.clicked.connect(self.button_to_exp)
        self.btn_6.clicked.connect(self.button_to_exp)
        self.btn_7.clicked.connect(self.button_to_exp)
        self.btn_8.clicked.connect(self.button_to_exp)
        self.btn_9.clicked.connect(self.button_to_exp)
        self.btn_close_bracket.clicked.connect(self.button_to_exp)
        self.btn_open_bracket.clicked.connect(self.button_to_exp)
        self.btn_point.clicked.connect(self.button_to_exp)
        self.btn_x.clicked.connect(self.button_to_exp)
        self.btn_div.clicked.connect(self.button_to_exp)
        self.btn_mul.clicked.connect(self.button_to_exp)
        self.btn_plus.clicked.connect(self.button_to_exp)
        self.btn_minus.clicked.connect(self.button_to_exp)
        self.btn_mod.clicked.connect(self.button_to_exp)
        self.btn_pow.clicked.connect(self.button_to_exp)
        self.btn_cos.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_sin.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_tan.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_acos.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_asin.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_atan.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_log.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_ln.clicked.connect(self.button_to_exp_with_bracket)
        self.btn_sqrt.clicked.connect(self.button_to_exp_with_bracket)
        # Credit buttons
        self.btn_calc_credit.clicked.connect(self.calculate_credit)
        # History buttons
        self.btn_hist_restore.clicked.connect(self.restore_exp_from_history)
        self.btn_hist_clear.clicked.connect(self.clear_history)
        self.list_hist.itemDoubleClicked.connect(self.restore_exp_from_history)

    def set_validators(self):
        custom_locale = QLocale.c()
        custom_locale.setNumberOptions(QLocale.RejectGroupSeparator)

        x_validator = QDoubleValidator(
            float('-inf'), float('inf'),
            -1,
            self
        )
        x_validator.setNotation(QDoubleValidator.StandardNotation)
        x_validator.setLocale(custom_locale)

        self.valueX.setValidator(x_validator)
        self.valueXMax.setValidator(x_validator)
        self.valueXMin.setValidator(x_validator)

        credit_validator = QDoubleValidator(0, float('inf'), 2, self)
        credit_validator.setNotation(QDoubleValidator.StandardNotation)
        credit_validator.setLocale(custom_locale)
        self.credit_principal.setValidator(credit_validator)
        self.credit_rate.setValidator(credit_validator)
        self.credit_term.setValidator(credit_validator)

    def parse_config(self):
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

        if 'Logging' in config:
            self._logging_period = config.get('Logging', 'period')

    def configure_logging(self):
        log_dir = os.path.join(self._current_dir, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(format=log_format, level=logging.INFO, handlers=[])

        interval = 1
        if self._logging_period == 'hour':
            rotation_period = 'H'
        elif self._logging_period == 'month':
            rotation_period = 'D'
            interval = 30
        else:
            rotation_period = 'D'

        log_file_name = os.path.join(log_dir, 'logs_{}.log'.format(
            datetime.now().strftime('%d-%m-%y-%H-%M-%S')))
        file_handler = logging.handlers.TimedRotatingFileHandler(
            log_file_name, when=rotation_period, interval=interval)
        file_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(file_handler)

    def button_to_exp(self, with_bracket: bool = False):
        if self._exp_evaluated:
            self.clear_result()
            self.exp_text_changed()

        button = self.sender()
        new_label = self.expressionText.text() + button.text() + \
            ("(" if with_bracket else "")
        self.exp_set_text_no_signals(new_label)

    def button_to_exp_with_bracket(self):
        self.button_to_exp(True)

    def exp_text_changed(self):
        self._exp_evaluated = False

    @Slot(bool)
    def on_tgl_calc_toggled(self, checked):
        self.calcX.setVisible(checked)
        self._mode_switched = True

    @Slot(bool)
    def on_tgl_graph_toggled(self, checked):
        self.graphX.setVisible(checked)

    def evaluate_exp(self):
        if self._exp_evaluated and self.tgl_calc.isChecked() and not self._mode_switched:
            return
        current_exp = self.expressionText.text()
        # Add entry to the history
        self.list_hist.insertItem(0, current_exp)
        # Log the operation
        logging.info('Operation performed: %s', current_exp)
        # Evaluate the expression
        if self.tgl_graph.isChecked():
            self.plot_graph_signal.emit(
                current_exp, self.valueXMin.text(), self.valueXMax.text())
        else:
            self.calc_exp_signal.emit(current_exp, self.valueX.text())
        self._exp_evaluated = True
        self._mode_switched = False

    def update_result(self, result):
        self.exp_set_text_no_signals(f"{result:.17g}")

    def calculation_error(self, error: str):
        self.exp_set_text_no_signals(error)

    def clear_result(self):
        self.exp_set_text_no_signals('')

    def open_graph(self, x, y):
        plot_window = ViewGraph(
            f"{self.expressionText.text()} ({self.valueXMin.text()} <= x <= {self.valueXMax.text()})")
        plot_window.plot_graph(x, y)
        plot_window.show()
        plot_window.destroyed.connect(
            lambda: self.remove_plot_window(plot_window))
        self._plot_windows.append(plot_window)

    def calculate_credit(self):
        self.calc_credit_signal.emit(
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

    def closeEvent(self, event):
        for plot_window in self._plot_windows:
            plot_window.close()
        self._plot_windows.clear()
        self.save_settings()
        super().closeEvent(event)

    def remove_plot_window(self, window):
        if window in self._plot_windows:
            self._plot_windows.remove(window)

    def restore_exp_from_history(self):
        current_expression = self.list_hist.currentItem()
        if current_expression:
            self.expressionText.setText(current_expression.text())
            self.tabWidget.setCurrentIndex(0)

    def clear_history(self):
        if self.list_hist.count() > 0:
            confirmation = QMessageBox.question(
                self,
                "Confirm history clean up", "Are you sure you want to clear the history?",
                QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                self.list_hist.clear()

    def save_settings(self):
        self._settings.beginWriteArray("history")
        for i in range(self.list_hist.count()):
            self._settings.setArrayIndex(i)
            self._settings.setValue(
                "expression", self.list_hist.item(i).text())
        self._settings.endArray()

    def restore_settings(self):
        size = self._settings.beginReadArray("history")
        for i in range(size):
            self._settings.setArrayIndex(i)
            value = self._settings.value("expression")
            if value is not None:
                self.list_hist.addItem(value)
        self._settings.endArray()

    def safe_config_getint(self, config, section, option, fallback=None):
        try:
            return config.getint(section, option, fallback=fallback)
        except ValueError:
            return fallback

    def exp_set_text_no_signals(self, text):
        self.expressionText.blockSignals(True)
        self.expressionText.setText(text)
        self.expressionText.blockSignals(False)
