### Virtual environment

```
python -m venv venv
pip install -r requirements.txt
```

### Generate the UI file

```
pyside6-uic view/s21_view.ui -o view/s21_view_ui.py
```

### Install the wrapper

```
python model/s21_setup.py install
```

### Compile the executable

```
pyinstaller --onefile -w --distpath installer/s21_SmartCalc_v3/packages/com.elidacon.s21_smartcalc_v3/data/ --name s21_SmartCalc_v3 s21_main.py 
```

### Compile the installer

```
D:/Coding/Qt/QtIFW-4.7.0/bin/binarycreator.exe -c installer/s21_SmartCalc_v3/config/config.xml -p installer/s21_SmartCalc_v3/packages/ installer/s21_SmartCalc_v3_installer.exe
```