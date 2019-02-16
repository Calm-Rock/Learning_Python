from cx_Freeze import setup, Executable

#We need to define what are we going to turn into an
#executable, what are we gonna call that executable.
#We can give description say, version number etc

setup(name='urlParser',
      version='1.0',
      description='Wanna mess with Google?',
      executables = [Executable("distme.py")])

#If a package has a lot of GUI stuff or is a lot graphical
#it becomes difficult to convert it to exe
#Example --> matplotlib
