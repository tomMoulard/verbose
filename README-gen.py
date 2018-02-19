import verbose
import time

v = verbose.Verbose(outputfile="README.md", level=10)
v.v("Verbose",1)
v.v("This is a simple way to manage the output for debug a python script.", 9)
v.v("And add some simple but effective results.", 9)

v.v("Verbosity level",2)
v.v("You can choose the verbosity level outputed on stdout when you initiate",9)
v.v("the class:", 9)
v.v("```python", 9)
v.v("v = verbose.Verbose(outputfile=\"README.md\", level=10)", 9)
v.v("```", 9)

v.v("Time", 2)
v.v("There is also a simple time capturing device:", 9)
v.v("```python", 9)
v.v("import time", 9)
v.v("v.timeOn(\"test\")", 9)
v.v("time.sleep(1)", 9)
v.v("t = v.timeOff(\"test\")", 9)
v.v("```", 9)
v.v("Now t is roughtly 1s", 9)


v.v("More output", 2)
v.v("You can also use some arguments in the function:", 9)

v.v("```python", 9)
v.v("v.v(\"The result is {}\", 9, kwargs = (t,))", 9)
v.v("```", 9)

v.v("The output file",2)
v.v("You have the choice to save (or not) the output of your script",9)
v.v("By default, this will not save it, but you can call \"saveOutput\"",9)
v.v("```python", 9)
v.v("v.saveOutput()", 9)
v.v("```", 9)

v.v("This file was generated with this script", 9)
v.v("(see [this](https://github.com/tomMoulard/verbose/blob/master/README-gen.py) file for the code)",9)
v.saveOutput()