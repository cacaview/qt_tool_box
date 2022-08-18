if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
start .\venv\Scripts\pythonw.exe .\lib\video\py_player_demo2.py