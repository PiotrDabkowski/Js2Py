from pyjs import PyJs
import pyjsstring
import pyjsnumber

PyJsString = pyjsstring.PyJsString
NaN = pyjsnumber.NaN
PyJsNumber = pyjsnumber.PyJsNumber


class PyJsNull(PyJs):
    def __repr__(self):
        return 'null'
        
    def __add__(self, other):
        if isinstance(other, PyJsString):
            return PyJsString('undefined'+other.toString())
        else:
            return other
            
    def __mul__(self, other):
        return PyJsNumber(0)
        
    def __div__(self, other):
        return PyJsNumber(0)
        
    def __sub__(self, other):
        return -other
        
    def __neg__(self):
        return -PyJsNumber(0)
        
        
PyJsNull = PyJsNull()

