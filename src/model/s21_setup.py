from setuptools import setup, Extension
import pybind11
import os

if __name__ == "__main__":
    env_var = "S21_SMARTCALC3_GCOV"
    gcov_flag = os.getenv(env_var, '0') == '1'
    # Different flags for linux and windows
    name = "s21_model_wrapper"
    if os.name == 'nt':
        cpp_args = ['/std:c++17']
        coverage_args = []
    else:
        cpp_args = ['-std=c++17']
        if gcov_flag:
            cpp_args += ['-fprofile-arcs', '-ftest-coverage', f'-D{env_var}']
            coverage_args = ['-lgcov']
            name = f"{name}_gcov"
        else:
            coverage_args = []

    # Get current path to connect C++ files
    current_path = os.path.dirname(__file__)
    # Setup the wrapper
    setup(
        name=name,
        version="0.1",
        ext_modules=[
            Extension(
                name,
                [os.path.join(current_path, "s21_model_wrapper.cc"),
                 os.path.join(current_path, "s21_model.cc")],
                include_dirs=[pybind11.get_include()],
                language="c++",
                extra_compile_args=cpp_args,
                extra_link_args=coverage_args
            ),
        ],
    )
