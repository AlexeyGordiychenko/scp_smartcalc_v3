from PySide6.QtWidgets import QApplication
from view_model.s21_view_model import ViewModel
from view.s21_view import View
from s21_model_wrapper import Model


if __name__ == "__main__":
    app = QApplication([])

    model = Model()
    view_model = ViewModel(model)

    window = View(view_model)
    window.show()

    app.exec()
