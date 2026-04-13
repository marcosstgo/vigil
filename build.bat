@echo off
echo Instalando dependencias...
pip install pyinstaller pystray pillow requests

echo Compilando Vigil...
pyinstaller ^
  --onefile ^
  --windowed ^
  --name "Vigil" ^
  --icon "vigil.ico" ^
  --add-data "agent.py;." ^
  --hidden-import pystray._win32 ^
  --hidden-import PIL._tkinter_finder ^
  vigil_tray.py

echo.
if exist dist\Vigil.exe (
    echo BUILD OK — dist\Vigil.exe
) else (
    echo BUILD FALLO
)
pause
