from base import *
from constructors.jsmath import Math
from constructors.jsdate import Date
from constructors.jsobject import Object
from host.console import console

# Now we have all the necessary items to create global environment for script
__all__ = ['Js', 'PyJsComma', 'PyJsStrictEq', 'PyJsStrictNeq',
           'PyJsException', 'PyJsBshift', 'Scope', 'PyExceptionToJs',
           'JsToPyException', 'JS_BUILTINS', 'appengine', 'set_global_object',
           'JsRegExp', 'PyJsException', 'PyExceptionToJs', 'JsToPyException']

# these were defined in base.py
builtins = ('true','false','null','undefined','Infinity',
            'NaN', 'console', 'String', 'Number', 'Boolean', 'RegExp',
            'Math', 'Date', 'Object')
            #Array, Function, JSON,   Error is done later :)
            # also some built in functions like eval...

def set_global_object(obj):
    PyJs.GlobalObject = obj



scope = dict(zip(builtins, [eval(e) for e in builtins]))
# Now add errors:
for name, error in ERRORS.iteritems():
    scope[name] = error

JS_BUILTINS = {k:v for k,v in scope.iteritems()}