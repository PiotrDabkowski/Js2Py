from pyjsfunction import PyJsMethod
from pyjs import PyJs

class PyJsBuiltin(PyJs):
    @property
    def constructor(self):
        return self.__init__
    
    @PyJsMethod
    def toString():
        return 'NotAvailable'

    @PyJsMethod
    def hasOwnProperty(name):
        if name in this.__dict__:
            return True #PyJsBool
        return False

    @PyJsMethod
    def isPrototypeOf(other):
        return False




    
        
