from timeit import timeit
from collections import namedtuple
from array import array

class Y:
    def __init__(self, x):
        self.x = x

    def s(self, x):
        return self.x + 1

class X(object):
    A = 10
    B = 2
    C = 4
    D = 9

    def __init__(self, x):
        self.x = x
        self.stack = []

    def s(self):
        pass

    def __add__(self, other):
        return self.x + other.x

    def s(self):
        return self.x + 1

    def another(self):
        return self.x*2

    def yet_another(self):
        return 300*30

def add(a,b):
    return a.x + b.x




t = X(1)


Type = None
try:
    print timeit("type(t) is X", "from __main__ import X,Y,namedtuple,array,t,add, Type", number=1000000)
except:
    pass