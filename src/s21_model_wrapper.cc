#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "s21_model.h"

namespace py = pybind11;

PYBIND11_MODULE(s21_model_wrapper, m) {
  py::class_<s21::Model>(m, "Model")
      .def(py::init<>())
      .def("parse_expression", &s21::Model::ParseExpression)
      .def("calculate", &s21::Model::Calculate, py::arg("x") = 0.0)
      .def("credit_annuity", &s21::Model::CreditAnnuity)
      .def("credit_differentiated", &s21::Model::CreditDifferentiated);
}
