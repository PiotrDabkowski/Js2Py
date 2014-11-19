
class FunctionPrototype:            
    def toString():
        if not this.is_callable():
            raise TypeError('toString is not generic!')
        argnum = this.code.__code__.co_argcount-2
        args = ', '.join(this.code.__code__.co_varnames[0:argnum])
        return 'function %s(%s) '%(this.func_name, args)+this.source
    
    def call():
        if not len(arguments):
            obj = this.Js(None)
        else:
            obj = arguments[0]
        if len(arguments)<=1:
            args = () 
        else:
            args = arguments[1]
        return this.call(obj, args)
    
    def apply():
        if not len(arguments):
            obj = this.Js(None)
        else:
            obj = arguments[0]
        if len(arguments)<=1:
            args = () 
        else:
            args = tuple(arguments[e] for e in xrange(1, len(arguments)))
        return this.call(obj, args)

    def bind(thisArg):
        if not this.is_callable():
            raise this.Js(TypeError)('this must be callable!')
        to_call = this
        if not len(arguments):
            obj = this.Js(None)
        else:
            obj = arguments[0]
        if len(arguments)<=1:
            args = ()
        else:
            args = tuple(arguments[e] for e in xrange(1, len(arguments)))
        if obj.is_undefined():
            def PyJsInlineTemp(this, arguments):
                args2 = args + tuple(arguments[e] for e in xrange(0, len(arguments)))
                return to_call(*args2)
        else:
            def PyJsInlineTemp(this, arguments):
                args2 = args + tuple(arguments[e] for e in xrange(0, len(arguments)))
                return to_call.call(obj, args2)
        return PyJsInlineTemp  # it will be automatically converted to js function :)



