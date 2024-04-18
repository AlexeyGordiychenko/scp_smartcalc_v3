#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "scp_model.h"

namespace py = pybind11;

#ifdef SCP_SMARTCALC3_GCOV
PYBIND11_MODULE(scp_model_wrapper_gcov, m) {
#else
PYBIND11_MODULE(scp_model_wrapper, m) {
#endif

  py::class_<scp::Model>(m, "Model")
      .def(py::init<>())
      .def("parse_expression", &scp::Model::ParseExpression)
      .def("calculate", &scp::Model::Calculate, py::arg("x") = 0.0)
      .def("credit_annuity", &scp::Model::CreditAnnuity)
      .def("credit_differentiated", &scp::Model::CreditDifferentiated);
  py::class_<scp::CreditResult>(m, "CreditResult")
      .def(py::init<>())
      .def_readwrite("monthly_start", &scp::CreditResult::monthly_start)
      .def_readwrite("monthly_end", &scp::CreditResult::monthly_end)
      .def_readwrite("over", &scp::CreditResult::over)
      .def_readwrite("total", &scp::CreditResult::total);
}
