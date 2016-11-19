import re

import datetime

from desc import *
from simplex import *
import six
from pyjsparser import PyJsParser

from conversions import *
PRIMITIVES = frozenset(['String', 'Number', 'Boolean', 'Undefined', 'Null'])
Infinity = float('inf')
NaN = float('nan')


def Type(obj):
    return obj.TYPE


# 8.6.2
class PyJs(object):
    TYPE = 'Object'
    IS_CONSTRUCTOR = False

    prototype = None
    Class = None
    extensible = True
    value = None

    own = {}

    def get_member(self, unconverted_prop):
        return self.get(to_string(unconverted_prop))

    def get(self, prop):
        assert type(prop)==unicode
        cand = self.get_property(prop)
        if cand is None:
            return undefined
        if is_data_descriptor(cand):
            return cand['value']
        if cand['get'].is_undefined():
            return undefined
        return cand['get'].call(self)

    def get_own_property(self, prop):
        assert type(prop) == unicode
        # takes py returns py
        return self.own.get(prop)

    def get_property(self, prop):
        assert type(prop) == unicode
        # take py returns py
        cand = self.get_own_property(prop)
        if cand:
            return cand
        if self.prototype is not None:
            return self.prototype.get_property(prop)

    def put(self, prop, val, throw=False):
        assert type(prop) == unicode
        # takes py, returns none
        if not self.can_put(prop):
            if throw:
                raise TypeError()
            return
        own_desc = self.get_own_property(prop)
        if is_data_descriptor(own_desc):
            self.own[prop]['value'] = val
            return
        desc = self.get_property(prop)
        if is_accessor_descriptor(desc):
            desc['set'].call(self, (val,))  # calling setter on own or inherited element
        else:  # new property
            self.own[prop] = {'value': val,
                              'writable': True,
                              'configurable': True,
                              'enumerable': True}

    def can_put(self, prop):  # to check
        assert type(prop) == unicode
        # takes py returns py
        desc = self.get_own_property(prop)
        if desc:  # if we have this property
            if is_accessor_descriptor(desc):
                return desc['set'].is_callable()  # Check if setter method is defined
            else:  # data desc
                return desc['writable']
        if self.prototype is None:
            return self.extensible
        inherited = self.prototype.get_property(prop)
        if inherited is None:
            return self.extensible
        if is_accessor_descriptor(inherited):
            return not inherited['set'].is_undefined()
        elif self.extensible:
            return inherited['writable']  # weird...
        return False

    def has_property(self, prop):
        assert type(prop) == unicode
        # takes py returns Py
        return self.get_property(prop) is not None

    def delete(self, prop, throw=False):
        assert type(prop) == unicode
        # takes py, returns py
        desc = self.get_own_property(prop)
        if desc is None:
            return True
        if desc['configurable']:
            del self.own[prop]
            return True
        if throw:
            raise TypeError()
        return False

    def default_value(self, hint=None):
        order = ('valueOf', 'toString')
        if hint == 'String' or (hint is None and self.Class == 'Date'):
            order = ('toString', 'valueOf')
        for meth_name in order:
            method = self.get(meth_name)
            if method is not None and method.is_callable():
                cand = method.call(self)
                if cand.is_primitive():
                    return cand
        raise MakeError('TypeError', 'Cannot convert object to primitive value')

    def define_own_property(self, prop, desc, throw):  # Internal use only. External through Object
        assert type(prop) == unicode
        # takes Py, returns Py
        # prop must be a Py string. Desc is either a descriptor or accessor.
        # Messy method -  raw translation from Ecma spec to prevent any bugs. # todo check this
        current = self.get_own_property(prop)

        extensible = self.extensible
        if not current:  # We are creating a new OWN property
            if not extensible:
                if throw:
                    raise TypeError()
                return False
            # extensible must be True
            if is_data_descriptor(desc) or is_generic_descriptor(desc):
                DEFAULT_DATA_DESC = {'value': undefined,  # undefined
                                     'writable': False,
                                     'enumerable': False,
                                     'configurable': False}
                DEFAULT_DATA_DESC.update(desc)
                self.own[prop] = DEFAULT_DATA_DESC
            else:
                DEFAULT_ACCESSOR_DESC = {'get': undefined,  # undefined
                                         'set': undefined,  # undefined
                                         'enumerable': False,
                                         'configurable': False}
                DEFAULT_ACCESSOR_DESC.update(desc)
                self.own[prop] = DEFAULT_ACCESSOR_DESC
            return True
        # therefore current exists!
        if not desc or desc == current:  # We don't need to change anything.
            return True
        configurable = current['configurable']
        if not configurable:  # Prevent changing params
            if desc.get('configurable'):
                if throw:
                    raise TypeError()
                return False
            if 'enumerable' in desc and desc['enumerable'] != current['enumerable']:
                if throw:
                    raise TypeError()
                return False
        if is_generic_descriptor(desc):
            pass
        elif is_data_descriptor(current) != is_data_descriptor(desc):
            # we want to change the current type of property
            if not configurable:
                if throw:
                    raise TypeError()
                return False
            if is_data_descriptor(current):  # from data to setter
                del current['value']
                del current['writable']
                current['set'] = undefined  # undefined
                current['get'] = undefined  # undefined
            else:  # from setter to data
                del current['set']
                del current['get']
                current['value'] = undefined  # undefined
                current['writable'] = False
        elif is_data_descriptor(current) and is_data_descriptor(desc):
            if not configurable:
                if not current['writable'] and desc.get('writable'):
                    if throw:
                        raise TypeError()
                    return False
            if not current['writable'] and 'value' in desc and current['value'] != desc['value']:
                if throw:
                    raise TypeError()
                return False
        elif is_accessor_descriptor(current) and is_accessor_descriptor(desc):
            if not configurable:
                if 'set' in desc and desc['set'] != current['set']:
                    if throw:
                        raise TypeError()
                    return False
                if 'get' in desc and desc['get'] != current['get']:
                    if throw:
                        raise TypeError()
                    return False
        current.update(desc)
        return True

    def create(self, *args):
        '''Generally not a constructor, raise an error'''
        raise MakeError('TypeError', '%s is not a constructor' % self.Class)


def get_member(self, prop, space): # general member getter, prop has to be unconverted prop. it is it can be any value
    typ = type(self)
    if typ not in PRIMITIVES:  # most likely getter for object
        return self.get_member(prop)  # <- object can implement this to support faster prop getting. ex array.
    elif typ == unicode:  # then probably a String
        if type(prop)==float:
            index = int(prop)
            if index==prop and 0 <= index < len(self):
                return self[index]
        s_prop = to_string(prop)
        if s_prop == 'length':
            return len(self)
        elif s_prop.isdigit():
            index = int(s_prop)
            if 0 <= index < len(self):
                return self[index]
        else:
            # use standard string prototype
            return space.StringPrototype.get(s_prop)
        # maybe an index
    elif typ == float:
        # use standard number prototype
        return space.NumberPrototype.get(to_string(prop))
    elif typ == bool:
        return space.BooleanPrototype.get(to_string(prop))
    elif typ is UNDEFINED_TYPE:
        raise MakeError('TypeError', "Cannot read property '%s' of undefined" % prop)
    elif typ is NULL_TYPE:
        raise MakeError('TypeError', "Cannot read property '%s' of null" % prop)
    else:
        raise RuntimeError('Unknown type! - ' + repr(typ))


def get_member_dot(self, prop, space):
    # dot member getter, prop has to be unicode
    typ = type(self)
    if typ not in PRIMITIVES:  # most likely getter for object
        return self.get(prop)
    elif typ == unicode:  # then probably a String
        if prop == 'length':
            return len(self)
        elif prop.isdigit():
            index = int(prop)
            if 0 <= index < len(self):
                return self[index]
        else:
            # use standard string prototype
            return space.StringPrototype.get(prop)
            # maybe an index
    elif typ == float:
        # use standard number prototype
        return space.NumberPrototype.get(prop)
    elif typ == bool:
        return space.BooleanPrototype.get(prop)
    elif typ in (UNDEFINED_TYPE, NULL_TYPE):
        raise MakeError('TypeError', "Cannot read property '%s' of undefined" % prop)
    else:
        raise RuntimeError('Unknown type! - ' + repr(typ))


# Object

class PyJsObject(PyJs):
    TYPE = 'Object'
    Class = 'Object'
    def __init__(self, prototype=None):
        self.extensible = True
        self.prototype = prototype
        self.own = {}

    def _init(self, props, vals, strict):
        i = 0
        for prop, kind in props:
            if prop in self.own: # just check... probably will not happen very often.
                if is_data_descriptor(self.own[prop]):
                    if kind!='i' or strict:
                        raise MakeError('SyntaxError', 'Invalid object initializer! Duplicate property name "%s"' % prop)
                else:
                    if kind=='i' or (kind=='g' and 'get' in self.own[prop]) or (kind=='s' and 'set' in self.own[prop]):
                        raise MakeError('SyntaxError', 'Invalid object initializer! Duplicate setter/getter of prop: "%s"' % prop)

            if kind == 'i': # init
                self.own[prop] = {'value': vals[i], 'writable': True, 'enumerable': True, 'configurable': True}
            elif kind == 'g': # get
                self.define_own_property(prop, {'get': vals[i], 'enumerable': True, 'configurable': True}, False)
            elif kind == 's': # get
                self.define_own_property(prop, {'get': vals[i], 'enumerable': True, 'configurable': True}, False)
            else:
                raise RuntimeError('Invalid property kind - %s. Expected one of i, g, s.' % repr(kind))
            i += 1

    def _set_props(self, prop_descs):
        for prop, desc in six.iteritems(prop_descs):
            self.define_own_property(prop, desc)




# Array

# todo Optimise Array - extremely slow due to index conversions from str to int and back etc.
# solution - make get and put methods callable with any type of prop and handle conversions from inside
# if not array then use to_string(prop). In array if prop is integer then just use it
# also consider removal of these stupid writable, enumerable etc for ints.
class PyJsArray(PyJs):
    Class = 'Array'
    def __init__(self, length, prototype=None):
        self.extensible = True
        self.prototype = prototype
        self.own = {'length' : {'value': length, 'writable': True,
                                'enumerable': False, 'configurable': False}}

    def _init_elements(self, elements):
        for i, ele in enumerate(elements):
            if ele is None: continue
            self.own[unicode(i)] = {'value': ele, 'writable': True,
                                    'enumerable': True, 'configurable': True}

    def put(self, prop, val, throw=False):
        # takes py, returns none
        if not self.can_put(prop):
            if throw:
                raise TypeError()
            return
        own_desc = self.get_own_property(prop)
        if is_data_descriptor(own_desc):
            self.define_own_property(prop, {'value': val}, False)
            return
        desc = self.get_property(prop)
        if is_accessor_descriptor(desc):
            desc['set'].call(self, (val,))  # calling setter on own or inherited element
        else:  # new property
            self.define_own_property(prop, {'value': val,
                                          'writable': True,
                                          'configurable': True,
                                          'enumerable': True}, False)


    def define_own_property(self, prop, desc, throw):
        old_len_desc = self.get_own_property('length')
        old_len = old_len_desc['value'].value  #  value is js type so convert to py.
        if prop=='length':
            if 'value' not in desc:
                return PyJs.define_own_property(self, prop, desc)
            new_len =  to_uint32(desc['value'])
            if new_len!=desc['value'].to_number().value:
                raise MakeError('RangeError', 'Invalid range!')
            new_desc = dict((k,v) for k,v in six.iteritems(desc))
            new_desc['value'] = new_len
            if new_len>=old_len:
                return PyJs.define_own_property(self, prop, new_desc)
            if not old_len_desc['writable']:
                return False
            if 'writable' not in new_desc or new_desc['writable']==True:
                new_writable = True
            else:
                new_writable = False
                new_desc['writable'] = True
            if not PyJs.define_own_property(self, prop, new_desc):
                return False
            if new_len<old_len:
                # not very efficient for sparse arrays, so using different method for sparse:
                if old_len>30*len(self.own):
                    for ele in self.own.keys():
                        if ele.isdigit() and int(ele)>=new_len:
                            if not self.delete(ele): # if failed to delete set len to current len and reject.
                                new_desc['value'] = old_len+1
                                if not new_writable:
                                    new_desc['writable'] = False
                                PyJs.define_own_property(self, prop, new_desc)
                                return False
                    old_len = new_len
                else: # standard method
                    while new_len<old_len:
                        old_len -= 1
                        if not self.delete(str(int(old_len))): # if failed to delete set len to current len and reject.
                            new_desc['value'] = old_len+1
                            if not new_writable:
                                new_desc['writable'] = False
                            PyJs.define_own_property(self, prop, new_desc)
                            return False
            if not new_writable:
                self.own['length']['writable'] = False
            return True

        elif prop.isdigit():
            index = to_uint32(prop)
            if index>=old_len and not old_len_desc['writable']:
                return False
            if not PyJs.define_own_property(self, prop, desc):
                return False
            if index>=old_len:
                old_len_desc['value'] = index + 1
            return True
        else:
            return PyJs.define_own_property(self, prop, desc)

    def to_list(self):
        return [self.get(str(e)) for e in xrange(self.get('length').to_uint32())]


# database with compiled patterns. Js pattern -> Py pattern.
REGEXP_DB = {}

class PyJsRegExp(PyJs):
    Class = 'RegExp'

    def __init__(self, body, flags, prototype=None):
        self.extensible = True
        self.prototype = prototype
        self.glob = True if 'g' in flags else False
        self.ignore_case = re.IGNORECASE if 'i' in flags else 0
        self.multiline = re.MULTILINE if 'm' in flags else 0
        self.value = body

        if (body, flags) in REGEXP_DB:
            self.pat = REGEXP_DB[body, flags]
        else:
            comp = None
            try:
                # converting JS regexp pattern to Py pattern.
                possible_fixes = [
                    (u'[]', u'[\0]'),
                    (u'[^]', u'[^\0]'),
                    (u'nofix1791', u'nofix1791')
                ]
                reg = self.value
                for fix, rep in possible_fixes:
                    comp = PyJsParser()._interpret_regexp(reg, flags)
                    #print 'reg -> comp', reg, '->', comp
                    try:
                        self.pat = re.compile(comp, self.ignore_case | self.multiline)
                        #print reg, '->', comp
                        break
                    except:
                        reg = reg.replace(fix, rep)
                       # print 'Fix', fix, '->', rep, '=', reg
                else:
                    raise
                REGEXP_DB[body, flags] = self.pat
            except:
                #print 'Invalid pattern...', self.value, comp
                raise MakeError('SyntaxError', 'Invalid RegExp pattern: %s -> %s'% (repr(self.value), repr(comp)))
        # now set own properties:
        self.own = {'source' : {'value': self.value, 'enumerable': False, 'writable': False, 'configurable': False},
                    'global' : {'value': self.glob, 'enumerable': False, 'writable': False, 'configurable': False},
                    'ignoreCase' : {'value': bool(self.ignore_case), 'enumerable': False, 'writable': False, 'configurable': False},
                    'multiline' : {'value': bool(self.multiline), 'enumerable': False, 'writable': False, 'configurable': False},
                    'lastIndex' : {'value': 0, 'enumerable': False, 'writable': True, 'configurable': False}}

    def match(self, string, pos):
        '''string is of course a py string'''
        return self.pat.match(string, pos)


class PyJsError(PyJs):
    Class = 'Error'
    extensible = True
    def __init__(self, message=None, prototype=None):
        self.prototype = prototype
        self.own = {}
        if message is not None:
            self.put('message', to_string(message))
            self.own['message']['enumerable'] = False



class PyJsDate(PyJs):
    Class = 'Date'
    UTCToLocal = None # todo UTC to local should be imported!

    def __init__(self, value, prototype=None):
        self.extensible = True
        self.value = value
        self.own = {}
        self.prototype = prototype

    # todo fix this problematic datetime part
    def to_local_dt(self):
        return datetime.datetime.utcfromtimestamp(self.UTCToLocal(self.value)//1000)

    def to_utc_dt(self):
        return datetime.datetime.utcfromtimestamp(self.value//1000)

    def local_strftime(self, pattern):
        if self.value is NaN:
            return 'Invalid Date'
        try:
            dt = self.to_local_dt()
        except:
            raise MakeError('TypeError', 'unsupported date range. Will fix in future versions')
        try:
            return dt.strftime(pattern)
        except:
            raise MakeError('TypeError', 'Could not generate date string from this date (limitations of python.datetime)')

    def utc_strftime(self, pattern):
        if self.value is NaN:
            return 'Invalid Date'
        try:
            dt = self.to_utc_dt()
        except:
            raise MakeError('TypeError', 'unsupported date range. Will fix in future versions')
        try:
            return dt.strftime(pattern)
        except:
            raise MakeError('TypeError', 'Could not generate date string from this date (limitations of python.datetime)')


#Function
class PyJsFunction(PyJs):
    Class = 'Function'
    source = '{ [native code] }'
    IS_CONSTRUCTOR = True

    def __init__(self, code, scope, params, name, space, prototype=None):
        self.extensible = True
        self.prototype = prototype
        self.own = {}

        self.code = code
        if type(self.code) == int: # just a label pointing to the beginning of the code.
            self.is_native = False
        else:
            self.is_native = True  # python function

        self.scope = scope
        self.params = params
        self.name = name
        self.space = space

        #set own property length to the number of arguments
        self.own['length'] = {'value': len(params), 'writable': False, 'enumerable': False, 'configurable': False}

        if name:
            self.own['name'] = {'value': name, 'writable': False, 'enumerable': False, 'configurable': True}

        if not self.is_native:  # set prototype for user defined functions
            # constructor points to this function
            proto = space.NewObject()
            proto.own['constructor'] = {'value': self, 'writable': True, 'enumerable': False, 'configurable': True}
            self.own['prototype'] = {'value': proto, 'writable': True, 'enumerable': False, 'configurable': False}
        # todo set up throwers on callee and arguments if in strict mode


    def call(self, this, args=()):
        ''' Dont use this method from inside bytecode to call other bytecode. '''
        if self.is_native:
            return self.code(this, args) # must return valid js object - undefined, null, float, unicode, bool, or PyJs
        else:
            return self.space.exe._call(self, this, args) # will run inside bytecode

    def has_instance(self, other):
        # I am not sure here so instanceof may not work lol.
        if not is_object(other):
            return False
        proto = self.get('prototype')
        if not proto.is_object():
            raise MakeError('TypeError', 'Function has non-object prototype in instanceof check')
        while True:
            other = other.prototype
            if not other:  # todo make sure that the condition is not None or null
                return False
            if other is proto:
                return True

    def create(self, args):
        proto = self.get('prototype')
        if not is_object(proto):
            proto = self.space.ObjectPrototype
        new = PyJsObject(prototype=proto)
        res = self.call(new, args)
        if is_object(res):
            return res
        return new