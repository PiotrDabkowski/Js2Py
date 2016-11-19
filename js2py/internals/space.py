from base import *

class Space(object):
    def __init__(self):
        self.GlobalCtx = None
        self.GlobalObj = None

        self.BooleanPrototype = None
        self.NumberPrototype = None
        self.StringPrototype = None

        self.FunctionPrototype = None
        self.ArrayPrototype = None
        self.DatePrototype = None
        self.ObjectPrototype = None

        self.ErrorPrototype = None
        self.EvalErrorPrototype = None
        self.RangeErrorPrototype = None
        self.ReferenceErrorPrototype = None
        self.SyntaxErrorPrototype = None
        self.TypeErrorPrototype = None
        self.URIErrorPrototype = None
        self.ERROR_TYPES = {
            'Error': self.ErrorPrototype,
            'EvalError': self.EvalErrorPrototype,
            'RangeError': self.RangeErrorPrototype,
            'ReferenceError': self.ReferenceErrorPrototype,
            'SyntaxError': self.SyntaxErrorPrototype,
            'TypeError': self.TypeErrorPrototype,
            'URIError': self.URIErrorPrototype,
        }

        self.interpreter = None

    def get_global_environment(self):
        return self.GlobalCtx.variable_environment()

    def NewObject(self):
        return PyJsObject(self.ObjectPrototype)

    def NewFunction(self, function_code, formal_parameter_list=[], scope=None, strict=False):
        return PyJsFunction(function_code, formal_parameter_list, scope, strict, )

    def NewDate(self, value):
        return PyJsDate(value, self.DatePrototype)

    def NewArray(self, length=0):
        return PyJsArray(length, self.ArrayPrototype)

    def NewError(self, typ, message):
        return PyJsError(message, self.ERROR_TYPES[typ])
