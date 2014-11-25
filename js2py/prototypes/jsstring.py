# -*- coding: utf-8 -*-
from jsregexp import Exec
import re
DIGS = set('0123456789')




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
        this.cok()
        s = this.to_string()
        r = this.RegExp(regexp)
        if r.glob:
            return Exec(r, s)
        r.put('lastIndex', this.Js(0))
        found = []
        last_index = n = 0
        while True:
            res = Exec(r, s)
            if res.is_null():
               break
            index = res.get('lastIndex').value
            if last_index==index:
                r.put('lastIndex', index+1)
                last_index = index + 1
            else:
                last_index = index
            found.append(res.get('0'))
            n += 1
        if not n:
            return this.null
        return this.Js(found)

    def replace(searchValue, replaceValue):
        # VERY COMPLICATED. to check again.
        this.cok()
        string = this.to_string()
        s = string.value
        res = ''
        if not replaceValue.is_callable():
            replaceValue = replaceValue.to_string().value
            func = False
        else:
            func = True
        # Replace all  ( global )
        if searchValue.Class == 'RegExp' and searchValue.glob:
            last = 0
            for e in re.finditer(searchValue.pat, s):
                res += s[last:e.span()[0]]
                if func:
                    # prepare arguments for custom func (replaceValue)
                    args = (e.group(),) +  e.groups() + (e.span()[1], string)
                    # convert all types to JS
                    args = tuple(this.Js(x) for x in args)
                    res += replaceValue(*args).to_string().value
                else:
                    res += replacement_template(replaceValue, s, e.span(), e.groups())
                last = e.span()[1]
            res += s[last:]
            return this.Js(res)
        elif searchValue.Class=='RegExp':
            e = re.search(searchValue.pat, s)
            if e is None:
                return string
            span = e.span()
            pars = e.groups()
            match = e.group()
        else:
            match = searchValue.to_string().value
            ind =  s.find(match)
            if ind==-1:
                return string
            span = ind, ind + len(match)
            pars = ()
        res = s[:span[0]]
        if func:
            args = (match,) +  pars + (span[1], string)
            # convert all types to JS
            args = tuple(this.Js(x) for x in args)
            res += replaceValue(*args).to_string().value
        else:
            res += replacement_template(replaceValue, s, span, pars)
        res += s[span[1]:]
        return this.Js(res)

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






def replacement_template(rep, source, span, npar):
    """Takes the replacement template and some info about the match and returns filled template
       """
    n = 0
    res = ''
    while n < len(rep)-1:
        char = rep[n]
        if char=='$':
            if rep[n+1]=='$':
                res += '$'
                n += 2
                continue
            elif rep[n+1]=='`':
                # replace with string that is BEFORE match
                res += source[:span[0]]
                n += 2
                continue
            elif rep[n+1]=='\'':
                # replace with string that is AFTER match
                res += source[span[1]:]
                n += 2
                continue
            elif rep[n+1] in DIGS:
                dig = rep[n+1]
                if n+2<len(rep) and rep[n+2] in DIGS:
                    dig += rep[n+2]
                num = int(dig)
                # we will not do any replacements if we dont have this npar or dig is 0
                if not num or num>len(npar):
                    res += '$'+dig
                else:
                    # None - undefined has to be replaced with ''
                    res += npar[num-1] if npar[num-1] else ''
                n += 1 + len(dig)
                continue
        res += char
        n += 1
    if n<len(rep):
        res += rep[-1]
    return res



































