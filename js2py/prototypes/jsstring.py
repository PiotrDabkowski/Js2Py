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

    def indexOf(searchString, position):
        this.cok()
        s = this.to_string().value
        search = searchString.to_stirng().value
        pos = position.to_int()
        return this.Js(s.find(search, min(max(pos, 0), len(s))) )

    def lastIndexOf(searchString, position):
        this.cok()
        s = this.to_string().value
        search = searchString.to_stirng().value
        pos = position.to_number()
        pos = 10**15 if pos.is_nan() else pos.to_int()
        return this.Js(s.rfind(search, 0, min(max(pos, 0)+1, len(s))) )

    def localeCompare (that):
        this.cok()
        s = this.to_string()
        that = that.to_string()
        if s<that:
            return this.Js(-1)
        elif s>that:
            return this.Js(1)
        return this.Js(0)

    def match(regexp):
        pass

    def replace(searchValue, replaceValue):
        pass

    def search(regexp):
        pass

    def slice(start, end):
        pass

    def split (separator, limit):
        pass

    def substring (start, end):
        pass

    def toLowerCase():
        pass

    def toLocaleLowerCase():
        pass

    def toUpperCase():
        pass

    def toLocaleUpperCase():
        pass

    def trim():
        pass










































