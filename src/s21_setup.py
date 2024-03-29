from setuptools import setup, Extension
import pybind11

setup(
    name="s21_model_wrapper",
    version="0.1",
    ext_modules=[
        Extension(
            "s21_model_wrapper",
            ["s21_model_wrapper.cc", "s21_model.cc"],
            include_dirs=[pybind11.get_include()],
            language="c++",
        ),
    ],
)
