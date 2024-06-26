## Building / running the application on Linux

1. Make sure you're in the src/ folder

1. Create virtual enviroment: `make venv`

1. Run:

    - without the executable: `make run`
    - compile the executable and run it: `make run_exe`
    - compile the installer and run it (you'll need to install Qt installer framework first): `make run_installer`

## Run tests and check coverage

1. Make sure you're in the src/ folder

1. To run tests: `make test`

1. To check coverage: `make gcov_report`


## Compile an installer for Windows in powershell

### Virtual environment

```
python -m venv venv
pip install -r requirements.txt
```

### Generate the UI file

```
pyside6-uic view/scp_view.ui -o view/scp_view_ui.py
```

### Install the wrapper

```
python model/scp_setup.py install
```

### Compile the executable

```
pyinstaller --onefile -w --distpath installer/scp_SmartCalc_v3/packages/com.elidacon.scp_smartcalc_v3/data/ --name scp_SmartCalc_v3 scp_main.py 
```

### Compile the installer

```
D:/Coding/Qt/QtIFW-4.7.0/bin/binarycreator.exe -c installer/scp_SmartCalc_v3/config/config.xml -p installer/scp_SmartCalc_v3/packages/ installer/scp_SmartCalc_v3_installer.exe
```