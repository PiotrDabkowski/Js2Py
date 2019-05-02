from __future__ import print_function
from ..base import *

@Js
def console():
    pass

@Js
def log():
    args = arguments
    print(*(args[i] for i in args))

console.put('log', log)
console.put('debug', log)
console.put('info', log)
console.put('warn', log)
console.put('error', log)
