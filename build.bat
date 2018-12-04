REM py -3.4 -m pip install py2exe installs py2exe.
REM this builder only works with python 3.4 as the bytecode was redesigned after


py -3.4 -m py2exe.build_exe bell.py
