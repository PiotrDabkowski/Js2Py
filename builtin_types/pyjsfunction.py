from pyjs import PyJs

class _PyJsFunction(PyJs):
    def __init__(self, func, name=None, PyJsClosure={}):
        '''Note PyJsClosure can have only one key name: this'''
        #if PyJsClosure.keys() not in [[], ['this']]:
        #    raise ValueError('Invalid PyJsClosure!')
        PyJsClosure['PyJSGlobals'] = func.func_globals
        self._PyJsFunc = func
        self._PyJsFuncArgcount = func.func_code.co_argcount
        self._PyJsFuncName = func.func_code.co_name if not name else name
        self._PyJsFuncVarnames = func.func_code.co_varnames
        self._PyJsClosure = PyJsClosure
        
    def __call__(self, *args):
        if 'this' in self._PyJsClosure:
            cp = {k:v for k,v in self._PyJsClosure['PyJSGlobals'].iteritems()}
            cp.update(self._PyJsClosure)
            cp['globals'] = lambda : self._PyJsClosure['PyJSGlobals']
            self._PyJsFunc = _list_to_func(_func_to_list(self._PyJsFunc), cp)
            del cp
        
        arguments = args # Here it should be argument object!
        method = 'self' in self._PyJsFuncVarnames
        _args = [] if not method else [self]
        for i, e in enumerate(args, method):
            if i==self._PyJsFuncArgcount:
                break
            _args.append(e)
        else:
            _args.extend((self._PyJsFuncArgcount - len(_args))*[None]) #Here should be undefined!
        del args
        self._PyJsFunc.func_globals['arguments'] = arguments
        self._PyJsFunc.func_globals.update(self._PyJsClosure)
        return self._PyJsFunc(*_args) #Here add smart type converter :)
        

def PyJsMethod(func): #Adds "this"
    @property
    def temp(self):
        return PyJsFunction(func, PyJsClosure={'this': self})
    return temp


class PyJsFunction(_PyJsFunction):
    @property
    def constructor(self):
        return PyJsFunction(self.__init__, 'Function')

    @property
    def name(self):
        return self._PyJsFuncName
    
    @PyJsMethod
    def valueOf():
        return this

    @PyJsMethod
    def toLocaleString():
        return this.toString()

    @PyJsMethod
    def hasOwnProperty(name):
        if hasattr(this, name):
            return True
        return False
        
    @PyJsMethod
    def toString():
        return 'function '+this._PyJsFuncName+'('+', '.join(this._PyJsFuncVarnames)+') { [Magic Python code] }'
    
    def __repr__(self):
        return self.toString()

    



def _func_to_list(func):
    '''converts a function to a special list'''
    args = ['argcount',
            'nlocals',
            'stacksize',
            'flags',
            'code',
            'consts',
            'names',
            'varnames',
            'filename',
            'name',
            'firstlineno',
            'lnotab',
            'freevars',
            'cellvars']
    func_code = [func.func_code.__getattribute__('co_'+e) for e in args]
    return func_code, {}

    
def _list_to_func(func_list, scope=False):
    '''conversts list to function'''
    return _func_to_list.__class__(_func_to_list.func_code.__class__(*func_list[0]), func_list[1] if not scope else scope)


dupa = 200

@PyJsFunction
def f(a,b):
    print a, b
    return arguments

@PyJsFunction
def g(x):
    pass
    




