import js2py.pyjs, sys
# Redefine builtin objects... Do you have a better idea?
for m in sys.modules.keys():
	if m.startswith('js2py'):
		del sys.modules[m]
del js2py.pyjs
del js2py
from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
PyJs_Object_0_ = Js({})
@Js
def PyJs_anonymous_1_(val, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'val':val}, var)
    var.registers([u'val'])
    var.put(u'f', var.get(u'val'))
PyJs_anonymous_1_._set_name(u'anonymous')
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return Js(9999.0)
PyJs_anonymous_2_._set_name(u'anonymous')
PyJs_Object_0_.define_own_property(u's', {"get":PyJs_anonymous_2_, 'configurable':True, 'enumerable': True})
PyJs_Object_0_.define_own_property(u's', {"set":PyJs_anonymous_1_, 'configurable':True, 'enumerable': True})

var.put(u'a', PyJs_Object_0_)
pass
print var.get('a')
pass
