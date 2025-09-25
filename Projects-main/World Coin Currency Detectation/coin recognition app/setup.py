import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"D:/Programs/Python/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = r"D:/Programs/Python/tcl/tk8.6"

executables = [cx_Freeze.Executable("gui.py", base=base)]


cx_Freeze.setup(
    name = "Currency Coin Detector",
    options = {"build_exe": {"packages":["tkinter","os","tensorflow","keras","json","ctypes","PIL","pandas","numpy","matplotlib"], "include_files":['tcl86t.dll','tk86t.dll', 'images','mobilenetv2_trained_model.h5']}},
    version = "1.0",
    description = "Currency Coin Detector can predict currency, its face value and country from which it belongs | Developed By Deepika & Saurabh",
    executables = executables
    )