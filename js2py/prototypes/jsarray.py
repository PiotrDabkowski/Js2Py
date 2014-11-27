# not implemented yet

class ArrayPrototype:
    def push():
        n = this.get('length').to_uint32()
        for e in arguments.to_list():
            this.put(str(n), e)
        this.own['length']['value'] = this.Js(n+len(arguments))

    def toString():
        res = []
        for e in xrange(len(this)):
            res.append(this.get(str(e)))
        return unicode(res)