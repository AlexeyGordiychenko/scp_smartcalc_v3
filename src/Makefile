QtIFW_FOLDER = ~/Qt/QtIFW-4.7.0
UI_PY = view/s21_view_ui.py
EXE_NAME = s21_SmartCalc_v3
INSTALLER_NAME = $(EXE_NAME)_installer.run
INSTALLER_DIR = installer
EXE_PATH = $(INSTALLER_DIR)/$(EXE_NAME)/packages/com.elidacon.s21_smartcalc_v3/data/

MODEL_DIR=model
SRCS_MODEL=$(wildcard $(MODEL_DIR)/s21_*.cc $(MODEL_DIR)/s21_*.h)
CPP_LIB_GCOV = dist/s21_model_wrapper_gcov-0.1-py3.11-linux-x86_64.egg
CPP_LIB = $(subst _gcov,,$(CPP_LIB_GCOV))

SRC_DIR=.
GCOV_DIR=gcov


all: run_exe

venv:
	python -m venv ../.venv && source ../.venv/bin/activate
	pip install -r requirements.txt

cpp: $(CPP_LIB)

cpp_gcov: $(CPP_LIB_GCOV)

ui: $(UI_PY)

run: cpp ui
	python s21_main.py

exe: $(EXE_PATH)/$(EXE_NAME)

run_exe: exe
	$(EXE_PATH)/$(EXE_NAME)

installer: $(INSTALLER_DIR)/$(INSTALLER_NAME)

$(CPP_LIB): $(SRCS_MODEL)
	export S21_SMARTCALC3_GCOV=0 && python $(MODEL_DIR)/s21_setup.py install

$(CPP_LIB_GCOV): $(SRCS_MODEL)
	export S21_SMARTCALC3_GCOV=1 && python $(MODEL_DIR)/s21_setup.py install

$(UI_PY): view/s21_view.ui
	pyside6-uic view/s21_view.ui -o $(UI_PY)

$(EXE_PATH)/$(EXE_NAME): cpp ui
	pyinstaller --onefile -w --distpath $(EXE_PATH) --name $(EXE_NAME) s21_main.py 

$(INSTALLER_DIR)/$(INSTALLER_NAME): $(EXE_PATH)/$(EXE_NAME)
	$(QtIFW_FOLDER)/bin/binarycreator -c $(INSTALLER_DIR)/$(EXE_NAME)/config/config.xml -p $(INSTALLER_DIR)/$(EXE_NAME)/packages/ $(INSTALLER_DIR)/$(INSTALLER_NAME)

test: cpp_gcov
	pytest

gcov_report: test
	mkdir -p $(GCOV_DIR)
	gcovr --html-details -o $(GCOV_DIR)/index.html --exclude $(MODEL_DIR)/s21_\.\*wrapper\.\*
	open $(GCOV_DIR)/index.html

lcov_report: test
	mkdir -p $(GCOV_DIR)
	lcov --capture --directory $(SRC_DIR) --exclude "$(CURDIR)/tests/*" --exclude "$(CURDIR)/model/*wrapper*" --output-file $(GCOV_DIR)/coverage.info --no-external
	genhtml -o $(GCOV_DIR) $(GCOV_DIR)/coverage.info 
	open $(GCOV_DIR)/index.html

clean:
	rm -rf dist build *.egg-info *.spec $(UI_PY) $(EXE_PATH)/$(EXE_NAME) $(INSTALLER_DIR)/$(INSTALLER_NAME) $(GCOV_DIR)