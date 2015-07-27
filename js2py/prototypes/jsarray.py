def to_arr(this):
    """Returns Python array from Js array"""
    return [this.get(str(e)) for e in xrange(len(this))]

class ArrayPrototype:
    def toString():
        # this function is wrong but I will leave it here fore debugging purposes.
        return unicode(to_arr(this))

    def toLocaleString():
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        # separator is simply a comma ', '
        if not arr_len:
            return ''
        res = []
        for i in xrange(arr_len):
            element = array[str(i)]
            if element.is_undefined() or element.is_null():
                res.append('')
            else:
                cand = element.to_object()
                str_func = element.get('toLocaleString')
                if not str_func.is_callable():
                    raise this.MakeError('TypeError', 'toLocaleString method of item at index %d is not callable'%i)
                res.append(element.callprop('toLocaleString'))
        return ', '.join(res)

    def concat():
        raise NotImplementedError()

    def join(separator):
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        separator = ',' if separator.is_undefined() else separator.to_string().value
        return separator.join(array.get(str(e)).to_string().value for e in xrange(arr_len))

    def pop():
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        if not arr_len:
            array.put('length', this.Js(arr_len))
            return None
        ind = str(arr_len-1)
        element = array.get(ind)
        array.delete(ind)
        array.put('length', this.Js(arr_len-1))
        return element


    def push(item):
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        to_put = arguments.to_list()
        for i, e in enumerate(to_put, arr_len):
            array.put(str(i), e)
        i += 1
        array.put('length', this.Js(i))
        return i


    def reverse():
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        lower, middle = 0, arr_len/2
        while lower!=middle:
            upper = arr_len - lower - 1
            ls, us = str(lower), str(upper)
            lower_val, upper_val = array.get(ls), array.get(us)
            lower_exists, upper_exists = array.has_property(ls), array.has_property(us)
            if lower_exists and upper_exists:
                array.put(us, lower_val)
                array.put(ls, upper_val)
            elif not lower_exists and upper_exists:
                array.put(ls, upper_val)
                array.delete(us)
            elif not lower_exists and upper_exists:
                array.put(us, lower_val)
                array.delete(ls)
            lower += 1
        return array


    def shift():
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        if not arr_len:
            array.put('length', this.Js(0))
            return None
        first = array.get('0')
        for k in xrange(1, arr_len):
            from_s, to_s = str(k), str(k-1)
            if array.has_property(from_s):
                array.put(to_s, array.get(from_s))
            else:
                array.delete(to)
        array.delete(str(arr_len-1))
        array.put('length', this.Js(str(arr_len-1)))
        return first

    def slice(start, end):
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        relative_start = start.to_int()
        k = max((arr_len + relative_start), 0) if relative_start<0 else  min(relative_start, arr_len)
        relative_end = arr_len if end.is_undefined() else end.to_int()
        final =  max((arr_len + relative_end), 0) if relative_end<0 else min(relative_end, arr_len)
        res = []
        n = 0
        while k<final:
            pk = str(k)
            if array.has_property(pk):
                res.append(array.get(pk))
            k += 1
            n += 1
        return res

    def sort(cmpfn):
        # I will implement it later because it seems to be a bit complicated
        # I will have to use built in sort function for speed reasons
        raise NotImplementedError()

    def splice(start, deleteCount):
        array = this.to_object()
        arr_len = array.get('length').to_uint32()
        relative_start = start.to_int()
        actual_start = max((arr_len + relative_start),0) if relative_start<0 else min(relative_start, arr_len)
        actual_delete_count =  min(max(deleteCount.to_int(),0 ), arr_len - actual_start)


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