QtIFW_FOLDER = ~/Qt/QtIFW-4.7.0
UI_PY = view/scp_view_ui.py
EXE_NAME = scp_SmartCalc_v3
INSTALLER_NAME = $(EXE_NAME)_installer.run
INSTALLER_DIR = installer
EXE_PATH = $(INSTALLER_DIR)/$(EXE_NAME)/packages/com.elidacon.scp_smartcalc_v3/data/

MODEL_DIR=model
SRCS_MODEL=$(wildcard $(MODEL_DIR)/scp_*.cc $(MODEL_DIR)/scp_*.h)
CPP_LIB_GCOV = dist/scp_model_wrapper_gcov-0.1-py3.11-linux-x86_64.egg
CPP_LIB = $(subst _gcov,,$(CPP_LIB_GCOV))

SRC_DIR=.
GCOV_DIR=gcov

VENV=../.venv
VENV_BIN=$(VENV)/bin
PYTHON=$(VENV_BIN)/python3
PYINSTALLER=$(VENV_BIN)/pyinstaller
PYSIDE6=$(VENV_BIN)/pyside6-uic
PYTEST=$(VENV_BIN)/pytest
GCOVR=$(VENV_BIN)/gcovr
LCOV=$(VENV_BIN)/lcov

all: run_exe

venv:
	python3.11 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt --no-warn-script-location

cpp: $(CPP_LIB)

cpp_gcov: $(CPP_LIB_GCOV)

ui: $(UI_PY)

run: cpp ui
	$(PYTHON) scp_main.py

exe: $(EXE_PATH)/$(EXE_NAME)

run_exe: exe
	$(EXE_PATH)/$(EXE_NAME)

run_installer: $(INSTALLER_DIR)/$(INSTALLER_NAME)
	$(INSTALLER_DIR)/$(INSTALLER_NAME)

$(CPP_LIB): $(SRCS_MODEL)
	export SCP_SMARTCALC3_GCOV=0 && $(PYTHON) $(MODEL_DIR)/scp_setup.py install

$(CPP_LIB_GCOV): $(SRCS_MODEL)
	export SCP_SMARTCALC3_GCOV=1 && $(PYTHON) $(MODEL_DIR)/scp_setup.py install

$(UI_PY): view/scp_view.ui
	$(PYSIDE6) view/scp_view.ui -o $(UI_PY)

$(EXE_PATH)/$(EXE_NAME): cpp ui
	$(PYINSTALLER) --onefile -w --distpath $(EXE_PATH) --name $(EXE_NAME) scp_main.py 

$(INSTALLER_DIR)/$(INSTALLER_NAME): $(EXE_PATH)/$(EXE_NAME)
	$(QtIFW_FOLDER)/bin/binarycreator -c $(INSTALLER_DIR)/$(EXE_NAME)/config/config.xml -p $(INSTALLER_DIR)/$(EXE_NAME)/packages/ $(INSTALLER_DIR)/$(INSTALLER_NAME)

test: cpp_gcov
	$(PYTEST)

gcov_report: test
	mkdir -p $(GCOV_DIR)
	$(GCOVR) --html-details -o $(GCOV_DIR)/index.html --exclude $(MODEL_DIR)/scp_\.\*wrapper\.\*
	open $(GCOV_DIR)/index.html

clean:
	rm -rf dist build *.egg-info *.spec $(UI_PY) $(EXE_PATH)/$(EXE_NAME) $(INSTALLER_DIR)/$(INSTALLER_NAME) $(GCOV_DIR)