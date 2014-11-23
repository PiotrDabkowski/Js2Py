# -*- coding: utf-8 -*-

class StringPrototype:
    def toString():
        if this.Class!='String':
            raise this.Js(TypeError)('String.prototype.toString is not generic')
        return this

    def valueOf():
        if this.Class!='String':
            raise this.Js(TypeError)('String.prototype.valueOf is not generic')
        return this

    # todo this should be in constructor
    def fromCharCode():
        args = arguments.to_list()
        res = u''
        for e in args:
            res +=unichr(e.to_uint16())
        return this.Js(res)

    def charAt(pos):
        this.cok()
        pos = pos.to_int()
        s = this.to_string()
        if 0<= pos < len(s.value):
            char = s.value[pos]
            if char not in s.CHAR_BANK:
                s.Js(char) # add char to char bank
            return s.CHAR_BANK[char]
        return s.CHAR_BANK['']

    def charCodeAt(pos):
        this.cok()
        pos = pos.to_int()
        s = this.to_string()
        if 0<= pos < len(s.value):
            return s.Js(ord(s.value[pos]))
        return s.NaN

    def concat():
        this.cok()
        s = this.to_string()
        res = s.value
        for e in arguments.to_list():
            res += e.to_string().value
        return this.Js(res)






