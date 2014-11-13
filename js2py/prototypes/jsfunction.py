
class FunctionPrototype:            
    def toString():
        if not this.is_callable():
            raise TypeError('toString is not generic!')
        argnum = this.code.__code__.co_argcount-2
        args = ', '.join(this.code.__code__.co_varnames[0:argnum])
        return 'function %s(%s) '%(this.func_name, args)+this.source
    
    def call():
        #change this code to do the same but operating on real arguments instad of tuple
        # remember that you need to supply a tuple to this.call so convert to tuple
        if not len(arguments):
            obj = this.undefined
        else:
            obj = arguments[0]
        if len(arguments)<=1:
            args = () 
        else:
            args = arguments[1]
        return this.call(obj, args)
    
    def apply():
        #change this code to do the same but operating on real arguments instad of tuple
        # remember that you need to supply a tuple to this.call so convert to tuple
        if not len(arguments):
            obj = this.undefined
        else:
            obj = arguments[0]
        if len(arguments)<=1:
            args = () 
        else:
            args = arguments[1:]
        return this.call(obj, args)
        
