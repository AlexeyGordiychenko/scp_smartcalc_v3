from setuptools import setup, Extension
import pybind11
import os

if os.name == 'nt':
    cpp_args = ['/std:c++17']
else:
    cpp_args = ['-std=c++17']

setup(
    name="s21_model_wrapper",
    version="0.1",
    ext_modules=[
        Extension(
            "s21_model_wrapper",
            ["s21_model_wrapper.cc", "s21_model.cc"],
            include_dirs=[pybind11.get_include()],
            language="c++",
            extra_compile_args=cpp_args,
        ),
    ],
)
