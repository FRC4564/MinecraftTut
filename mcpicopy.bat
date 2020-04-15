rem Copy mcpi folder to the Python 3.8 library
mkdir %SYSTEMDRIVE%\Users\%USERNAME%\AppData\Local\Programs\Python\Python38-32\Lib\mcpi
copy /v mcpi\*.* %SYSTEMDRIVE%\Users\%USERNAME%\AppData\Local\Programs\Python\Python38-32\Lib\mcpi\
pause

