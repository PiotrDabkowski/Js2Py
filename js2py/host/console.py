from ..base import *
class Console:
    def log(self, *args, **kwargs):
        print(*args, **kwargs)

    def debug(self, *args, **kwargs):
        print(*args, **kwargs)

    def info(self, *args, **kwargs):
        print(*args, **kwargs)

    def warn(self, *args, **kwargs):
        print(*args, **kwargs)

    def error(self, *args, **kwargs):
        print(*args, **kwargs)

@Js
def console():
    pass

@Js
def log():
    print(" ".join(repr(element) for element in arguments.to_list()))

console.put('log', log)
console.put('debug', log)
console.put('info', log)
console.put('warn', log)
console.put('error', log)
