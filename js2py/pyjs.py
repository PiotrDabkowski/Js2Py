from base import *
from constructors import jsobject
from host.console import console

# Now we have all the necessary items to create global environment for script
__all__ = ['Js', 'PyJsComma', 'PyJsStrictEq', 'PyJsStrictNeq',
           'PyJsException', 'PyJsBshift', 'Scope', 'PyExceptionToJs',
           'JsToPyException', 'JS_BUILTINS', 'appengine', 'set_global_object',
           'JsRegExp']

# these were defined in base.py
builtins = ('true','false','null','undefined','Infinity',
            'NaN', 'console', 'String')
           #'Number', 'Boolean', 'String', 'Array', 'Object',

def set_global_object(obj):
    PyJs.GlobalObject = obj



scope = dict(zip(builtins, [eval(e) for e in builtins]))
JS_BUILTINS = {k:v for k,v in scope.iteritems()}