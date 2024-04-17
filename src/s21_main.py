import sys
from PySide6.QtWidgets import QApplication
from view_model.s21_view_model import ViewModel
from view.s21_view import View
from s21_model_wrapper import Model
import os


if __name__ == "__main__":
    # Get the current path from the executable or the main .py file if running
    # manually
    if getattr(sys, 'frozen', False):
        current_path = os.path.dirname(sys.executable)
    else:
        current_path = os.path.dirname(__file__)

    app = QApplication([])
    app.setStyle('Fusion')

    model = Model()
    view_model = ViewModel(model)

    view = View(view_model, current_path)
    view.show()

    app.exec()
