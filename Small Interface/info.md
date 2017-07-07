I use cx Freeze to convert Python to exe.<br/>
To download it, type <code>python -m pip install cx_Freeze --upgrade</code><br/>
Then we should create <code>.py</code> file <br/>
Type something like that: <br?>
<pre class:brush="python">from cx_Freeze import setup, Executable #setup.py 
setup(name="Tkinter",
	version = "0.1",
	description="Tkinter interface",
	executables = [Executable("module.py")])</pre>
