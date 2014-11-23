
class RegExpPrototype:
    def toString():
        flags = u''
        if this.glob:
            flags += u'g'
        if this.ignore_case:
            flags += u'i'
        if this.multiline:
            flags += u'm'
        return u'/%s/'%self.value + flags

    def test(string):
        pass




def Exec(this, string):
    pass