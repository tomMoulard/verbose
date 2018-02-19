# -*- coding: utf-8 -*-
"""
Created on Mon Fev 19 2018

@author: tomMoulard
"""

class Verbose():
    def __init__(self, outputfile="", level=0):
        """
        :outputfile -> file name if you want to save the output
        :level      -> output level to display your messages on stdout
        """
        self.time       = __import__("time")
        self.outputfile = outputfile
        self.level      = level
        self.res        = []
        self.times      = {}

    def v(self, string, level, kwargs=()):
        if kwargs:
            string = string.format(*kwargs)
        if self.level > level:
            print("[{}:{}:{}] {}".format(*self.time.gmtime()[3:6], string))
        for x in range(level):
            string = "#" + string
        self.res.append(string)

    def timeOn(self, name):
        self.times[name] = self.time.time()

    def timeOff(self, name):
        t1 = self.times[name]
        t2 = self.time.time()
        return t2 - t1

    def saveOutput(self):
        if self.outputfile:
            with open(self.outputfile, "w") as f:
                for lines in self.res:
                    f.write(lines + "\n")
        else:
            name = "output-{}{}{}-{}:{}:{}.txt".format(*self.time.gmtime()[:6])
            with open(name, "w") as f:
                for lines in self.res:
                    f.write(lines + "\n")