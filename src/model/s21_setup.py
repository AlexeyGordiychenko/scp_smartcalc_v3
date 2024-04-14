from setuptools import setup, Extension
import pybind11
import os

if os.name == 'nt':
    cpp_args = ['/std:c++17']
else:
    cpp_args = ['-std=c++17']

curr_dir = os.path.dirname(__file__)
setup(
    name="s21_model_wrapper",
    version="0.1",
    ext_modules=[
        Extension(
            "s21_model_wrapper",
            [os.path.join(curr_dir, "s21_model_wrapper.cc"),
             os.path.join(curr_dir, "s21_model.cc")],
            include_dirs=[pybind11.get_include()],
            language="c++",
            extra_compile_args=cpp_args,
        ),
    ],
)
