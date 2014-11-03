
class FunctionPrototype:            
    def toString():
        if not this.is_callable():
            raise TypeError('toString is not generic!')
        argnum = this.code.func_code.co_argcount-2
        args = ', '.join(this.code.func_code.co_varnames[0:argnum])
        return 'function %s(%s) { [native code]}'%(this.func_name, args)
    
    def call(obj, args):
        return this.call(obj, args)
    
    def apply(obj):
        return this.call(obj, arguments[1:])
        
        
