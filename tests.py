# -*- coding: utf-8 -*-

from jstools.increments import *

def f():
    x =[0]
    def k():
        print x[0]
        x[0]+=1
    return k

PyJsAssign('g', locals(), PyJsAssign())