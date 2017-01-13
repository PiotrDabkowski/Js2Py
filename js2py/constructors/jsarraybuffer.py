# this is based on jsarray.py

# Actually, I don't really know, how buffers work, so it might be buggy af

from ..base import *
import numpy

@Js
def ArrayBuffer():
    a = arguments[0]
    if isinstance(a, PyJsNumber):
        length = a.to_uint32()
        if length!=a.value:
            raise MakeError('RangeError', 'Invalid array length')
        temp = Js(bytearray([0]*length))
        return temp
    return Js(bytearray([0]))

ArrayBuffer.create = ArrayBuffer
ArrayBuffer.own['length']['value'] = Js(None)

ArrayBuffer.define_own_property('prototype', {'value': ArrayBufferPrototype,
                                         'enumerable': False,
                                         'writable': False,
                                         'configurable': False})

ArrayBufferPrototype.define_own_property('constructor', {'value': ArrayBuffer,
                                                    'enumerable': False,
                                                    'writable': False,
                                                    'configurable': True})
