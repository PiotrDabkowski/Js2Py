__all__ = ['example']

# Don't look below, you wont understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'sayHello', u'someVariable', u'Rectangle', u'$nonPyName'])
@Js
def PyJsHoisted_sayHello_(name, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
    var.registers([u'name'])
    var.get(u'console').callprop(u'log', ((Js(u'Hello, ')+var.get(u'name'))+Js(u'!')))
PyJsHoisted_sayHello_.func_name = u'sayHello'
var.put(u'sayHello', PyJsHoisted_sayHello_)
@Js
def PyJsHoisted_Rectangle_(w, h, this, arguments, var=var):
    var = Scope({u'this':this, u'h':h, u'arguments':arguments, u'w':w}, var)
    var.registers([u'h', u'w'])
    var.get(u"this").put(u'w', var.get(u'w'))
    var.get(u"this").put(u'h', var.get(u'h'))
PyJsHoisted_Rectangle_.func_name = u'Rectangle'
var.put(u'Rectangle', PyJsHoisted_Rectangle_)
@Js
def PyJsHoistedNonPyName(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u'console').callprop(u'log', Js(u'Non-Py names like $ can be used too!'))
PyJsHoistedNonPyName.func_name = u'$nonPyName'
var.put(u'$nonPyName', PyJsHoistedNonPyName)
PyJs_Object_0_ = Js({u'a':Js(1.0),u'b':Js(2.0)})
var.put(u'someVariable', PyJs_Object_0_)
pass
pass
pass
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return (var.get(u"this").get(u'w')*var.get(u"this").get(u'h'))
PyJs_anonymous_2_._set_name(u'anonymous')
PyJs_Object_1_ = Js({u'getArea':PyJs_anonymous_2_})
var.get(u'Rectangle').put(u'prototype', PyJs_Object_1_)
var.put(u'x', var.get(u'Rectangle').create(Js(10.0), Js(10.0)))


# Add lib to the module scope
example = var.to_python()