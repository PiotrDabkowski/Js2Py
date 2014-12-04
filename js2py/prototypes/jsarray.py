def to_arr(this):
    """Returns Python array from Js array"""
    return [this.get(str(e)) for e in xrange(len(this))]

class ArrayPrototype:
    def toString():
        # this function is wrong but I will leave it here fore debugging purposes.
        return unicode(to_arr(this))

    def toLocaleString():
        raise NotImplementedError()

    def concat():
        raise NotImplementedError()

    def join(separator):
        raise NotImplementedError()

    def pop():
        raise NotImplementedError()

    def push():
        n = this.get('length').to_uint32()
        for e in arguments.to_list():
            this.put(str(n), e)
        this.own['length']['value'] = this.Js(n+len(arguments))

    def reverse():
        raise NotImplementedError()

    def shift():
        raise NotImplementedError()

    def slice(start, end):
        raise NotImplementedError()

    def sort(cmpfn):
        raise NotImplementedError()

    def splice(start, deleteCount):
        raise NotImplementedError()

    def unshift():
        raise NotImplementedError()

    def indexOf(searchElement):
        raise NotImplementedError()

    def lastIndexOf(searchElement):
        raise NotImplementedError()

    def every(callbackfn):
        raise NotImplementedError()

    def some(callbackfn):
        raise NotImplementedError()

    def forEach(callbackfn):
        raise NotImplementedError()

    def map(callbackfn):
        raise NotImplementedError()

    def filter(callbackfn):
        raise NotImplementedError()

    def reduce(callbackfn):
        raise NotImplementedError()

    def reduceRight(callbackfn):
        raise NotImplementedError()