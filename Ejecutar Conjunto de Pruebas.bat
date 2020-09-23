echo. ##################### ACTIVACION DEL ENTORNO VIRTUAL #####################
E:\SeleniumWithPython\environment\Scripts\activate.bat

echo. ##################### TEST PATH #####################
e:
cd E:\SeleniumWithPython\src\test

@echo off

echo. ##################### PRUEBAS #####################


python -m pytest test_001.py test_002.py test_003.py --junitxml=results.xml



pause