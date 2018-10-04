from ..base import *

@Js
def console():
    pass

@Js
def log():
    print(' '.join(map(str, arguments.to_list())))

console.put('log', log)