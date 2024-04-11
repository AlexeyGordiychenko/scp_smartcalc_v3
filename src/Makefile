all: run_exe

cpp:
	python3 s21_setup.py install

ui:
	pyside6-uic s21_view.ui -o s21_view_ui.py

run: ui
	python3 s21_main.py

exe:
	pyinstaller --onefile -w --distpath installer/s21_SmartCalc_v3/packages/com.elidacon.s21_smartcalc_v3/data --name s21_SmartCalc_v3 s21_main.py 

installer:
	~/Qt/QtIFW-4.7.0/bin/binarycreator -c installer/s21_SmartCalc_v3/config/config.xml -p installer/s21_SmartCalc_v3/packages/ installer/s21_SmartCalc_v3.run

run_exe: cpp ui exe
	./installer/s21_SmartCalc_v3/packages/com.elidacon.s21_smartcalc_v3/data/s21_SmartCalc_v3

clean:
	rm -rf dist *.egg-info build .spec