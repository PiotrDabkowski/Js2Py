'''A class representing all PyJs Objects.

_in dict format:

{'value': Number or String or None,
 'attrs': {attr_name: _in_dict, ...},
 'type': string returned by typeof,
 'extensible': bool,
 'configurable_attr': set([attr_name_list]),
 'call': python_function <- this keyword will be equal to self.
}
 

'''

from pyjs_templates import *
from injector import append_arguments
import types
import copy

class PyJsException(Exception): pass

def PyToPyJs(python_object, method_of=None):
    if isinstance(python_object, PyJs):
        return python_object
    elif isinstance(python_object, dict):
        return PyJs(python_object, True, method_of)
    elif isinstance(python_object, bool):
        return true if python_object else false
    elif isinstance(python_object, int) or isinstance(python_object, float) or isinstance(python_object, long):
        temp = PyJs(PyJsNumberTemplate)
        temp.__dict__['_PyJsIn']['value'] = python_object
        return temp
    elif isinstance(python_object, basestring):
        temp = PyJs(PyJsStringTemplate)
        temp.__dict__['_PyJsIn']['value'] = python_object
        return temp
    elif isinstance(python_object, types.FunctionType):
        PyJsFunctionTemplate['call'] = python_object
        return PyJs(PyJsFunctionTemplate, True, method_of)
    elif python_object is None:
        return undefined
    else:
        raise RuntimeError('Could not convert python value({}) to PyJs type'.format(python_object))

false = False
true = True
undefined = None

class PyJs(object):
    def __init__(self, _in, deepcopy=False, method_of=None):
        if _in.get('call'):
            self.__dict__['_PyJsFuncGlobals'] = _in['call'].func_globals
            func = _in['call']
            vvv = (('this',) if 'this' in func.func_code.co_varnames else ()) + (('arguments',) if 'arguments' in func.func_code.co_varnames else ())
            self.__dict__['_PyJsFuncCall']= append_arguments(_in['call'].func_code, vvv)
        self.__dict__['_PyJsIn'] = copy.deepcopy(_in) if deepcopy else {e:v for e,v in _in.iteritems()}
        self.__dict__['_PyJsMethodOf'] = method_of
        
        
    def __getattr__(self, attr): #modify for getters and setters
       if attr.startswith('__') or attr.startswith('_PyJs'):
           return self.__dict__[attr]
       return PyToPyJs(self.__dict__['_PyJsIn']['attrs'].get(attr), self)

    def __setattr__(self, attr, val):#modify for getters and setters
        self.__dict__[attr] = PyToPyJs(val)._PyJsIn
        
    def __getitem__(self, attr):#modify for getters and setters
        return PyToPyJs(self.__dict__['_PyJsIn']['attrs'].get(attr), self)

    def __setitem(self, attr, val):#modify for getters and setters
        self.__dict__[attr] = PyToPyJs(val)._PyJsIn
    
    def __repr__(self):
        return self.toString()
    
    def __call__(self, *args): 
        func_code = self.__dict__.get('_PyJsFuncCall')
        if not func_code:
            raise PyJsException('Object not callable!')
        this = self.__dict__.get('_PyJsMethodOf') if self.__dict__.get('_PyJsMethodOf') else self
        vvv = ((this,) if 'this' in func_code.co_varnames else ()) + ((arguments,) if 'arguments' in func_code.co_varnames else ())
        print vvv
        func = types.FunctionType(func_code, self.__dict__['_PyJsFuncGlobals'], argdefs=vvv) #here should be new Array(args)
        argnum = func.func_code.co_argcount-len(vvv)
        _args = args[:min(argnum, len(args))]+max(argnum-len(args),0)*(None,) #here should be undefined
        return func(*_args) #PyToPyJS should be here.
    
    def __mul__(self, other):
        print other
        
    def __add__(self, other):
        print other

    def __sub__(self, other):
        print other

    def __neg__(self):
        print 'neg'

    def __div__(self, other):
        print other

    def __cmp__(self, other):
        print other

    
    
    
        
