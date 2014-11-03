'''Most important file in Js2Py implementation: PyJs class - father of all PyJs objects'''
from injector import fix_js_args

def Js(val):
    '''Converts Py type to PyJs type'''
    if isinstance(val, PyJs):
        return val
    elif val is None:
        return undefined
    elif isinstance(val, basestring):
        return PyJsString(val, StringPrototype)
    elif isinstance(val, bool):
        return true if val else false
    elif isinstance(val, float) or isinstance(val, int) or isinstance(val, long):
        return PyJsNumber(float(val), NumberPrototype)
    elif isinstance(val, tuple): # convert to arguments
        return val # todo later
    else:
        raise RuntimeError('Cant convert python type to js')
        
def is_data_descriptor(desc):
    return desc and ('value' in desc or 'writable' in desc)
    
def is_accessor_descriptor(desc):
    return desc and ('get' in desc or 'set' in desc)
    
def is_generic_descriptor(desc):
    return desc and not (is_data_descriptor(desc) or is_accessor_descriptor(desc))
    
this = globals()  # this should be a global object...

##############################################################################

class PyJs:
    PRIMITIVES =  set(('String', 'Number', 'Boolean', 'Undefined', 'Null'))
    Class = None
    extensible = True
    prototype = None
    own = {}
    value = None
    
    def __init__(self, value=None, prototype=None, extensible=False):
        '''Constructor for Number String and Boolean'''
        if self.Class=='String' and not isinstance(value, basestring):
            raise TypeError
        if self.Class=='Number':
            if not isinstance(value, float):
                if not (isinstance(value, int) or isinstance(value, long)):
                    raise TypeError
                value = float(value)
        if self.Class=='Boolean' and not isinstance(value, bool):
            raise TypeError
        self.value = value
        self.extensible = extensible
        self.prototype = prototype
        self.own = {}
        
    def is_undefined(self):
        return self.Class=='Undefined'
    
    def is_null(self):
        return self.Class=='Null'
        
    def is_primitive(self):
        return self.Class in self.PRIMITIVES
    
    def is_object(self):
        return not self.is_primitive()
    
    def is_callable(self):
        return not self.is_primitive() and hasattr(self, 'call')
        
    def typ(self):
        typ = self.Class
        if self.is_primitive():
            return typ
        return 'Object'
            
    def typeof(self): 
        if self.is_callable():
            return Js('function')
        return Js(self.typ().lower())
    
    def get_own_property(self, prop):
        return self.own.get(prop)
    
    def get_property(self, prop):
        cand = self.get_own_property(prop)
        if cand:
            return cand
        if self.prototype is not None:
            return self.prototype.get_property(prop)
    
    def get(self, prop): #external use!
         #prop = prop.value
         if self.Class=='Undefined' or self.Class=='Null':
             raise TypeError('Undefiend and null dont have properties!')
         if not isinstance(prop, basestring): raise RuntimeError('Bug')
         cand = self.get_property(prop)
         if cand is None:
             return Js(None)
         if is_data_descriptor(cand): 
             return cand['value']
         if cand['get'].is_undefined():
             return cand['get']
         return cand['get'].call(self)
    
    def can_put(self, prop):  #to check
        desc = self.get_own_property(prop)
        if desc: #if we have this property
            if is_accessor_descriptor(desc):
                return desc['set'].is_callable() # Check if setter method is defined           
            else:  #data desc 
                return desc['writable']
        if self.prototype is not None:
            return self.extensible
        inherited = self.get_property(prop)
        if inherited is None:
            return self.extensible
        if is_accessor_descriptor(inherited):
            return not inherited['set'].is_undefined()
        elif self.extensible:
            return inherited['writable']
        return False
            
    
    def put(self, prop, val):  #external use!
        if self.Class=='Undefined' or self.Class=='Null':
             raise TypeError('Undefiend and null dont have properties!')
        #prop = prop.value
        if not isinstance(prop, basestring): raise RuntimeError('Bug')
        if not self.can_put(prop):
            return val
        own_desc = self.get_own_property(prop)
        if is_data_descriptor(own_desc):
            own_desc['value'] = val
            return val
        desc = self.get_property(prop)
        if is_accessor_descriptor(desc):
            desc['set'].call(self, val)
        else:
            self.own[prop] = {'value' : val, 
                              'writable' : True,
                              'configurable' : True,
                              'enumerable' : True}
        return val
                
    def has_property(self, prop):
        return self.get_property(prop) is not None
    
    def delete(self, prop):
        desc = self.get_own_property(prop)
        if desc is None: 
            return Js(True)
        if desc['configurable']:
            del self.own[prop]
            return Js(True)
        return Js(False)
    
    def default_value(self, hint=None):
        order = ['toString', 'valueOf']
        if hint=='Number' or (hint is None and self.Class=='Date'):
            order.reverse()
        for meth_name in order:
            method = self.get(meth_name)
            if method is not None and method.is_callable():
                cand = method.call(self)
                if cand.is_primitive():
                    return cand
        raise TypeError('Cannot convert object to primitive value')
        
    def define_own_property(self, prop, desc): #Internal use only. External through Object
        #Messy method -  raw translation from Ecma spec to prevent any bugs.
        current = self.get_own_property(prop)
        
        extensible = self.extensible
        default_data_desc = {'value': undefined, #undefined
                             'writable': False, 
                             'enumerable': False,
                             'configurable': False}
        default_accessor_desc = {'get': undefined, #undefined
                                 'set': undefined, #undefined
                                 'enumerable': False,
                                 'configurable': False}
        if not current: #We are creating a new property
            if not extensible:
                return False
            if is_data_descriptor(desc) or is_generic_descriptor(desc):
                default_data_desc.update(desc)
                self.own[prop] = default_data_desc
            else:
                default_accessor_desc.update(desc)
                self.own[prop] = default_accessor_desc
            return True
        
        if not desc or desc==current: #We dont need to change anything.
            return True
        configurable = current['configurable']  
        if not configurable:  #Prevent changing configurable or enumerable
            if desc['configurable']:
                return False
            if desc['enumerable']!=current['enumerable']:
                return False
        if is_generic_descriptor(desc):
            pass
        elif is_data_descriptor(current)!=is_data_descriptor(desc):
            if not configurable:
                return False
            if is_data_descriptor(current):
                del current['value']
                del current['writable']
                current['set'] = undefined #undefined
                current['get'] = undefined #undefined
            else:
                del current['set']
                del current['get']
                current['value'] = undefined #undefined
                current['writable'] = False 
        elif is_data_descriptor(current) and is_data_descriptor(desc):
            if not configurable:
                if not current['writable'] and desc['writable']:
                    return False
            if not current['writable'] and 'value' in desc and current['value']!=desc['value']:
                return False
        elif is_accessor_descriptor(current) and is_accessor_descriptor(desc):
            if not configurable:
                if 'set' in desc and desc['set'] is not current['set']:
                    return False
                if 'get' in desc and desc['get'] is not current['get']:
                    return False
        current.update(desc)
        return True
    
    #Type Conversions. to_type. All must return pyjs subclass instance
    
    def to_primitive(self, hint=None):
        if self.is_primitive():
            return self
        return self.default_value(hint)
            
    def to_boolean(self):
        typ = self.Class
        if typ=='Boolean':
            return self
        elif typ=='Null' or typ=='Undefined':
            return false
        elif typ=='Number' or typ=='String':
            return Js(bool(self.value and self.value==self.value)) # test for nan (nan -> flase)
        else: #object
            return true
            
    def to_number(self):
        typ = self.Class
        if typ=='Null':
            return Js(0)
        elif typ=='Undefined':
            return NaN
        elif typ=='Boolean':
            return Js(int(self.value))
        elif typ=='Number':
            return self
        elif typ=='String':
            s = self.value.strip() #Strip white space
            if not s: # '' is simply 0
                return Js(0)
            if 'x' in s or 'X' in s: #hex (positive only)
                try: # try to convert
                    num = int(s, 16)
                except ValueError: # could not convert > NaN
                    return NaN
                return num
            sign = 1 #get sign
            if s[0] in '+-':
                if s=='-': 
                    sign = -1
                s = s[1:]
            if s=='Infinity': #Check for infinity keyword. 'NaN' will be NaN anyway.
                return Js(sign*float('inf'))
            try: #decimal try
                num = sign*float(s) # Converted
            except ValueError:
                return NaN # could not convert to decimal  > return NaN
            return Js(num) 
        else: #object
            return self.to_primitive('Number').to_number()
            
    def to_string(self):
        typ = self.Class
        if typ=='Null':
            return Js('null')
        elif typ=='Undefined':
            return Js('undefined')
        elif typ=='Boolean':
            return Js('true') if self.value else Js('false')
        elif typ=='Number':
            if self.is_nan():
                return Js('NaN')
            elif self.is_infinity():
                return Js('Infinity')
            elif self.value.is_integer():  # dont print .0 
                return Js(str(int(self.value)))
            return Js(str(self.value)) # accurate enough
        elif typ=='String':
            return self
        else: #object
            return self.to_primitive('String').to_string() 
            
            
    def to_object(self):
        typ = self.Class
        if typ=='Null' or typ=='Undefined':
            raise TypeError('')
        elif typ=='Boolean': # Unsure here...
            return self
        elif typ=='Number':
            return self
        elif typ=='String':
            return self
        else: #object
            return self
    
    def same_as(self, other):
        typ = self.Class
        if typ!=other.Class:
            return False
        if typ=='Undefined' or typ=='Null':
            return True
        if typ=='Boolean' or typ=='Number' or typ=='String':
            return self.value==other.value
        else: #object
            return self is other #Id compare.
                
    #Oprators-------------
    #Unary, other will be implemented as functions. Increments and decrements 
    # will be methods of Number class
    def __neg__(self): #-u
        return Js(-self.to_number().value)
    
    def __pos__(self): #+u
        return self.to_number()
    
    def __inv__(self): #~u
        return Js(~self.to_number().value)
    
    def neg(self): # !u  cant do 'not u' :(
        return Js(not self.to_boolean().value)
    
    def __nonzero__(self): 
        return self.to_boolean().value
        
    # Additive operators
    # + and - are implemented here
        
    #+
    def __add__(self, other):
        a = self.to_primitive()
        b = other.to_primitive()
        if a.Class=='String' or b.Class=='String':
            return Js(a.to_string().value+b.to_string().value)
        a = a.to_number()
        b = b.to_number()
        return Js(a.value+b.value)
    
    #-
    def __sub__(self, other):
        return Js(self.to_number().value-other.to_number().value)
    
    #Multiplicative operators
    # *, / and % are implemented here
    
    #*
    def __mul__(self, other):
        return Js(self.to_number().value*other.to_number().value)
        
    #/
    def __div__(self, other):
        a = self.to_number().value
        b = other.to_number().value
        if b:
            return Js(a/b)
        if not a or a!=a:
            return NaN
        return Infinity if a>0 else -Infinity
    
    #%
    def __mod__(self, other):
        a = self.to_number().value
        b = other.to_number().value
        if abs(a)==float('inf') or not b:
            return NaN
        if abs(b)==float('inf'):
            return Js(a)
        pyres = Js(a%b) #different signs in python and javascript
                        #python has the same sign as b and js has the same 
                        #sign as a.
        if a<0 and pyres>0:
            pyres -= b
        elif a>0 and pyres<0:
            pyres += b
        return Js(pyres)
        
    #Comparisons (I dont implement === and !== here, these
    # will be implemented by external functions)
    # <, <=, !=, ==, >=, > are implemented here.
    #<
    def __lt__(self, other): 
        pass
    
    #<=
    def __le__(self, other): 
        pass
    
    #!=
    def __ne__(self, other): 
        pass
    
    #==
    def __eg__(self, other): 
        pass
    
    #>=
    def __ge__(self, other): 
        pass
    
    #>
    def __gt__(self, other): 
        pass
    
    #iteration
    def __iter__(self):
        #Returns a generator of all own enumerable properties
        return (Js(name) for name in self.own if self.own[name]['enumerable'])
    
    def contains(self, other):
        return Js(self.has_property(other.to_string().value))
        
    #Other Special methods
    def __call__(self, *args):
        if not self.is_callable():
            raise TypeError('%s is not a function'%self.typeof())
        return self.call(this, args) # global value of this 
    
    def __repr__(self):
        return self.to_string().value
    
    def callprop(self, prop, *args):
        #print 'Called callprop on prop %s with %d arguments'%(prop, len(args))
        cand = self.get(prop)
        if not cand.is_callable():
            raise TypeError('%s is not a function'%cand.typeof())
        return cand.call(self, args)

  
  
  
##############################################################################
#Define types
    
#Object
class PyJsObject(PyJs):
    Class = 'Object'
    def __init__(self, prop_descs={}, prototype=None, extensible=True):
        self.prototype = prototype
        self.extensible = extensible
        self.own = {}
        for prop, desc in prop_descs.iteritems():
            self.define_own_property(prop, desc)
    

ObjectPrototype = PyJsObject()


#Function
class PyJsFunction(PyJs):
    Class = 'Function'
    def __init__(self, func, prototype=None, extensible=True, source=None):
        func = fix_js_args(func)
        self.code = func
        self.source = source if source else '{ [python code] }'
        self.func_name = func.func_name if func.func_name!='PyJsInlineTemp' else ''
        self.extensible = extensible
        self.prototype = prototype
        self.own = {}
    
    def call(self, this, args=()):
        if not hasattr(args, '__iter__'):  #get rid of it later
            args = (args,)
        args = tuple(Js(e) for e in args)
        #print 'Calling function', self.func_name
        #print ('We have %d args'%len(args)), args
        #func has these arguments (some args, this, arguments)
        arguments = Js(args) # tuple will be converted to arguments object.
        arglen = self.code.func_code.co_argcount - 2 #function expects this number of args.
        if len(args)>arglen:
            args = args[0:arglen]
        elif len(args)<arglen:
            args += (Js(None),)*(arglen-len(args))
        args += this, arguments  #append extra params to the arg list
        return Js(self.code(*args))

def Empty():
    return Js(None)
    
FunctionPrototype = PyJsFunction(Empty, ObjectPrototype)


#Number
class PyJsNumber(PyJs):  #Note i dont implement +0 and -0. Just 0.
    Class = 'Number'
    INF = float('inf')
    NAN = float('nan')
    def is_infinity(self):
        return abs(self.value)==self.INF
        
    def is_nan(self):
        return self.value!=self.value

NumberPrototype = PyJsObject({}, ObjectPrototype)
Infinity = PyJsNumber(float('inf'), NumberPrototype)
NaN = PyJsNumber(float('nan'), NumberPrototype)


#String
class PyJsString(PyJs):
    Class = 'String'

StringPrototype = PyJsObject({}, ObjectPrototype)


#Boolean
class PyJsBoolean(PyJs):
    Class = 'Boolean'

BooleanPrototype = PyJsObject({}, ObjectPrototype) 
true = PyJsBoolean(True, BooleanPrototype)
false = PyJsBoolean(False, BooleanPrototype)


#Undefined
class PyJsUndefined(PyJs):
    Class = 'Undefined'
    def __init__(self):
        pass

undefined = PyJsUndefined()


#Null
class PyJsNull(PyJs):
    Class = 'Null'
    def __init__(self):
        pass
null = PyJsNull()

##############################################################################
# Import and fill prototypes here.

def fill_prototype(prototype, Class, attrs={'writable':True, 'enumerable':False, 'configurable':True}):
    for i in dir(Class):
        e = getattr(Class, i)
        if hasattr(e, '__func__'):
            temp = PyJsFunction(e.__func__, FunctionPrototype)
            attrs = {k:v for k,v in attrs.iteritems()}
            attrs['value'] = temp
            prototype.define_own_property(i, attrs)
            
from prototypes import jsfunction, jsobject, jsnumber, jsstring, jsboolean
#Object proto
fill_prototype(ObjectPrototype, jsobject.ObjectPrototype)
#Define __proto__
def __proto__(): 
    return this.prototype if this.prototype is not None else null
getter = PyJsFunction(__proto__, FunctionPrototype)
def __proto__(): pass
setter =  PyJsFunction(__proto__, FunctionPrototype)     
ObjectPrototype.define_own_property('__proto__', {'set': setter,
                                                  'get': getter,
                                                  'enumerable': False,
                                                  'configurable':True})
print ObjectPrototype.own['__proto__']
#Function proto
fill_prototype(FunctionPrototype, jsfunction.FunctionPrototype)  
#Number proto
fill_prototype(NumberPrototype, jsnumber.NumberPrototype)  
#String proto
fill_prototype(StringPrototype, jsstring.StringPrototype) 
#Boolean proto
fill_prototype(BooleanPrototype, jsboolean.BooleanPrototype)
 
 
print 'Started test'
 #test
if __name__=='__main__':
    print ObjectPrototype.get('toString').callprop('call')
    print FunctionPrototype.own
    a=  null-Js(49404)
    x = a.put('ser', Js('der'))
    print Js(0) or Js('p') and Js(4.0000000000050000001)
    FunctionPrototype.put('Chuj', Js(409))
    for e in FunctionPrototype:
        print 'Obk', e.get('__proto__').get('__proto__').get('__proto__'), e
        