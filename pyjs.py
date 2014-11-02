'''Most important file in Js2Py implementation: PyJs class - father of all PyJs objects'''

def Js(val):
    '''Converts Py type to PyJs type'''
    return val

def is_data_decriptor(desc):
    return desc and ('value' in desc or 'writable' in desc)
    
def is_accessor_descriptor(desc):
    return desc and ('get' in desc or 'set' in desc)
    
def is_generic_descriptor(desc):
    return desc and (is_data_decriptor(desc) or is_accessor_descriptor(desc))
    
NaN = 0
Undefined = 0
Infinity = float('inf')
true = 1
false = 0
    
class PyJs:
    PRIMITIVES =  set(('String', 'Number', 'Boolean', 'Undefined', 'Null'))
    Class = 'Base'
    extensible = True
    prototype = None
    own = {}
    value = None
    
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
        if self.Class=='Function':
            return 'function'
        return self.typ().lower()
    
    def get_own_property(self, prop):
        return self.own.get(prop)
    
    def get_property(self, prop):
        cand = self.get_own_property(prop)
        if cand:
            return cand
        if self.prototype:
            return self.prototype.get_property(prop)
    
    def get(self, prop): #external use!
         #prop = prop.value
         if not isinstance(prop, basestring): raise RuntimeError('Bug')
         cand = self.get_property(prop)
         if cand is None:
             return Js(None)
         if is_data_decriptor(cand): 
             return cand['value']
         if cand['get'].is_undefined():
             return cand['get']
         return cand['get'].call(self)
    
    def can_put(self, prop):  #to check
        desc = self.get_own_property(prop)
        if desc: #if we have this property
            if is_data_decriptor(desc):  #data desc
                return desc['writable']
            else:  #accessor desc 
                return not desc['set'].is_undefined()
        proto = self.prototype
        if proto is None and self.extensible:
            return True
        inherited = self.get_property(prop)
        if inherited is None:
            return self.extensible
        if is_data_decriptor(inherited):
            if not self.extensible:
                return False
            return inherited['writable']
        else:
            return not inherited['set'].is_undefined()
    
    def put(self, prop, val):  #external use!
        #prop = prop.value
        if not isinstance(prop, basestring): raise RuntimeError('Bug')
        if not self.can_put(prop):
            return val
        own_desc = self.get_own_property(prop)
        if is_data_decriptor(own_desc):
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
            return True
        return False
    
    def default_value(self, hint=None):
        order = ['toString', 'valueOf']
        if hint=='Number' or (hint is None and self.Class=='Date'):
            order.reverse()
        for meth_name in order:
            method = self.get(meth_name)
            if method.is_callable():
                cand = method.call(self)
                if cand.is_primitive():
                    return cand
        raise TypeError('Could not compute default value!')
        
    def define_own_property(self, prop, desc): #Internal use only. External through Object
        #Messy method -  raw translation from Ecma spec to prevent any bugs.
        print desc
        current = self.get_own_property(prop)
        extensible = self.extensible
        
        default_data_desc = {'value': None, #undefined
                             'writable': False, 
                             'enumerable': False,
                             'configurable': False}
        default_accessor_desc = {'get': None, #undefined
                                 'set': None, #undefined
                                 'enumerable': False,
                                 'configurable': False}
        if not current: #We are creating a new property
            if not extensible:
                return False
            if is_data_decriptor(desc) or is_generic_descriptor(desc):
                default_data_desc.update(desc)
                self.own[prop] = default_data_desc
            else:
                default_accessor_desc.update(desc)
                self.own[prop] = default_data_desc
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
        elif is_data_decriptor(current)!=is_data_decriptor(desc):
            if not configurable:
                return False
            if is_data_decriptor(current):
                del current['value']
                del current['writable']
                current['set'] = None #undefined
                current['get'] = None #undefined
            else:
                del current['set']
                del current['get']
                current['value'] = None #undefined
                current['writable'] = False 
        elif is_data_decriptor(current) and is_data_decriptor(desc):
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
            return Js(bool(self.value))
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
            return Js('Null')
        elif typ=='Undefined':
            return Js('Undefined')
        elif typ=='Boolean':
            return Js('true') if self.value else Js('false')
        elif typ=='Number':
            if self.is_NaN():
                return Js('NaN')
            elif self.is_infinity():
                return Js('Infinity')
            return Js(str(self.value)) # accurate enough
        elif typ=='String':
            return self
        else: #object
            self.to_primitive('String').to_string() 
            
            
    def to_object(self):
        typ = self.Class
        if typ=='Null' or typ=='Undefined':
            raise TypeError('')
        elif typ=='Number':
            pass
        elif typ=='String':
            pass
        else: #object
            return self
        
    
                
    #Oprators
    
        
    #Other Special methods
    def __call__(self, *args):
        raise TypeError('%s is not a function'%self.typeof())
    

  
    
print 'No syntax errors'

a = PyJs()

x = a.put('Slon', 594)
b = a.put('Slon', 594903032230)
print a.delete('Slond')
print a.get('Slon'), x, b