# Verbose
===
This is a simple way to manage the output for debug a python script.
And add some simple but effective results.
## Verbosity level
You can choose the verbosity level outputed on stdout when you initiate
the class:
```python
v = verbose.Verbose(outputfile="README.md", level=10)
```
## Time
There is also a simple time capturing device:
```python
import time
v.timeOn("test")
time.sleep(1)
t = v.timeOff("test")
```
Now t is roughtly 1s
## More output
You can also use some arguments in the function:
```python
v.v("The result is {}", 9, kwargs = (t,))
```
## The output file
You have the choice to save (or not) the output of your script
By default, this will not save it, but you can call "saveOutput"
```python
v.saveOutput()
```
This file was generated with this script
(see [this](https://github.com/tomMoulard/verbose/blob/master/README-gen.py) file for the code)
