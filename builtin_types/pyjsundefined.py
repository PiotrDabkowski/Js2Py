from pyjs import PyJs
import pyjsstring
import pyjsnumber

PyJsString = pyjsstring.PyJsString
NaN = pyjsnumber.NaN

class PyJsUndefined(PyJs):
    def __repr__(self):
        return 'undefined'
        
    def __add__(self, other):
        if isinstance(other, PyJsString):
            return PyJsString('undefined'+other.toString())
        else:
            return NaN
            
    def __mul__(self, other):
        return NaN
        
    def __div__(self, other):
        return NaN
        
    def __sum__(self, other):
        return NaN
    
    def __neg__(self):
        return NaN
        
PyJsUndefined = PyJsUndefined()
