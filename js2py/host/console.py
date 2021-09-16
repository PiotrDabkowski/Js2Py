from ..base import *

@Js
def console():
    pass

@Js
def log():
    print(*arguments.to_list())

console.put('log', log)
console.put('debug', log)
console.put('info', log)
console.put('warn', log)
console.put('error', log)
