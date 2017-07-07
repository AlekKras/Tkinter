from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6" #your path might be different
os.environ['TK_LIBRARY'] = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6" #your path might be different

setup(name="Tkinter",
	version = "0.1",
	description="Tkinter interface",
	executables = [Executable("module.py")])
