from ..base import *

@Js
def console():
    pass

@Js
def log():
    print(*arguments.to_list())

console.put('log', log)