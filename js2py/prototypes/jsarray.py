def to_arr(this):
    """Returns Python array from Js array"""
    return [this.get(str(e)) for e in xrange(len(this))]

class ArrayPrototype:
    def toString():
        # this function is wrong but I will leave it here fore debugging purposes.
        return unicode(to_arr(this))

    def toLocaleString():
        pass

    def concat():
        pass

    def join(separator):
        pass

    def pop():
        pass

    def push():
        n = this.get('length').to_uint32()
        for e in arguments.to_list():
            this.put(str(n), e)
        this.own['length']['value'] = this.Js(n+len(arguments))

    def reverse():
        pass

    def shift():
        pass

    def slice(start, end):
        pass

    def sort(cmpfn):
        pass

    def splice(start, deleteCount):
        pass

    def unshift():
        pass

    def indexOf(searchElement):
        pass

    def lastIndexOf(searchElement):
        pass

    def every(callbackfn):
        pass

    def some(callbackfn):
        pass

    def forEach(callbackfn):
        pass

    def map(callbackfn):
        pass

    def filter(callbackfn):
        pass

    def reduce(callbackfn):
        pass

    def reduceRight(callbackfn):
        pass