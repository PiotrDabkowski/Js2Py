from copy import copy as cp, deepcopy as dp

PyJsFunctionTemplate = {'value':None,
                        'attrs': {},
                        'call': None
                        }
toString_ = cp(PyJsFunctionTemplate)
def toString(k):
    f = this._PyJsFuncCall
    return 'function '+f.co_name+'('+', '.join(f.co_varnames)+') { [Python Code] }'
    
toString_['call'] = toString
PyJsFunctionTemplate['attrs']['toString'] = toString_ 
