from setuptools import setup, Extension
import pybind11
import os

if __name__ == "__main__":
    # Different flags for linux and windows
    if os.name == 'nt':
        cpp_args = ['/std:c++17']
    else:
        cpp_args = ['-std=c++17']

    # Get current path to connect C++ files
    current_path = os.path.dirname(__file__)
    # Setup the wrapper
    setup(
        name="s21_model_wrapper",
        version="0.1",
        ext_modules=[
            Extension(
                "s21_model_wrapper",
                [os.path.join(current_path, "s21_model_wrapper.cc"),
                 os.path.join(current_path, "s21_model.cc")],
                include_dirs=[pybind11.get_include()],
                language="c++",
                extra_compile_args=cpp_args,
            ),
        ],
    )
