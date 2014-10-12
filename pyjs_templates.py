from copy import copy as cp, deepcopy as dp
from PyJsObject import PyJs

def add_method(met, obj):
    temp = cp(obj)
    temp['call'] = met
    obj['attrs'][met.func_name] = temp

def compose_template(cls):
    template = cls._template
    for e in dir(cls):
        if e.startswith('_'): continue
        add_method(getattr(cls, e).__func__, template)
    globals()['PyJs'+cls.__name__] = template





class FunctionTemplate:
    _template = {'value':None,
                'attrs': {},
                'call': None
                }
    def toString():
        f = this._PyJsFuncCall
        args = []
        for e in f.co_varnames:
            if e in ['this', 'arguments']:
                break
            args.append(e)
        return 'function ' + f.co_name + '(' + ', '.join(args)+') { [Python Code] }'

    def valueOf():
        return this

    def zabol(a , b , c):
        print a
        return arguments, this





compose_template(FunctionTemplate)