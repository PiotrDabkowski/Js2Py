""" This module removes all objects/arrays from JS source code and replace them with LVALS.
Also it has  s function translating removed object/array to python code.
Use this module just after removing constants. Later move on to removing functions"""
OBJECT_LVAL = 'PyJsLvalObject%d_'
ARRAY_LVAL = 'PyJsLvalArray%d_'
from utils import *
from jsparser import *
from nodevisitor import  exp_translator


def is_empty_object(n, last):
    if n.strip():
        return False
    # seems to be but can be empty code
    last = last.strip()
    markers = {')', ';',}
    if not last or last[-1] in markers:
        return False
    return True

def is_array(last):
    #it can be prop getter
    last = last.strip()
    markers = {')', ']'}
    return not last or  not (last[-1] in markers or last[-1] in IDENTIFIER_PART)

def remove_objects(code, count=1):
    """ This function replaces objects with OBJECTS_LVALS, returns new code, replacement dict and count.
        count arg is the number that should be added to the LVAL of the first replaced object
    """
    replacements = {} #replacement dict
    br = bracket_split(code, ['{}', '[]'])
    res = ''
    last = ''
    for e in br:
        #test whether e is an object
        if e[0]=='{':
            n, temp_rep, cand_count = remove_objects(e[1:-1], count)
            # if e was not an object then n should not contain any :
            if ':' in n or is_empty_object(n, last):
                #e was an object
                res += OBJECT_LVAL % count
                replacements[OBJECT_LVAL % count] = e
                count += 1
            else:
                # e was just a code block but could contain objects inside
                res += '{%s}' % n
                count = cand_count
                replacements.update(temp_rep)
        elif e[0]=='[':
            if is_array(last):
                res += e  # will be translated later
            else: # prop get
                n, rep, count = remove_objects(e[1:-1], count)
                res += '[%s]' % n
                replacements.update(rep)
        else: # e does not contain any objects
            res += e
        last = e #needed to test for this stipid empty object
    return res, replacements, count


def remove_arrays(code, count=1):
    """removes arrays and replaces them with ARRAY_LVALS
       returns new code and replacement dict
       *NOTE* has to be called AFTER remove objects"""
    res = ''
    last = ''
    replacements = {}
    for e in bracket_split(code, ['[]']):
        if e[0]=='[' and is_array(last):
            name = ARRAY_LVAL % count
            res += name
            replacements[name] = e
            count += 1
        else:
            res += e
        last = e
    return res, replacements, count


def translate_object(obj, lval, obj_count=1, arr_count=1):
    obj = obj[1:-1] # remove {} from both ends
    obj, obj_rep, obj_count = remove_objects(obj, obj_count)
    obj, arr_rep, arr_count = remove_arrays(obj, arr_count)
    gsetters_after = ''
    keys = argsplit(obj)
    res = []
    for i, e in enumerate(keys, 1):
        e = e.strip()
        if e.startswith('set '):
            gsetters_after += translate_setter(lval, e)
        elif e.startswith('get '):
            gsetters_after += translate_getter(lval, e)
        elif ':' not in e:
            if i<len(keys): # can happen legally only in the last element {3:2,}
                raise SyntaxError('Unexpected "," in Object literal')
            break
        else: #Not getter, setter or elision
            key, value = e.split(':')
            key = key.strip().__repr__()
            value = exp_translator(value)
            if not value:
                raise SyntaxError('Missing value in Object literal')
            res.append('%s:%s' % (key, value))
    res = '%s = Js({%s})\n' % (lval, ','.join(res)) + gsetters_after
    for lval, obj in obj_rep.iteritems():
        new_def, obj_count, arr_count = translate_object(obj, lval, obj_count, arr_count)
        # add object definition BEFORE array definition
        res = new_def + res
    for lval, obj in arr_rep.iteritems():
        new_def, obj_count, arr_count = translate_array(obj, lval, obj_count, arr_count)
        # add object definition BEFORE array definition
        res = new_def + res
    return res, obj_count, arr_count



def translate_setter(lval, setter):
    trans = ''
    return trans

def translate_getter(lval, getter):
    trans = ''
    return trans


def translate_array(array, lval, obj_count=1, arr_count=1):
    """array has to be any js array for example [1,2,3]
       lval has to be name of this array.
       Returns python code that adds lval to the PY scope it should be put before lval"""
    array = array[1:-1]
    array, obj_rep, obj_count = remove_objects(array, obj_count)
    array, arr_rep, arr_count = remove_arrays(array, arr_count)
    arr = []
    for e in argsplit(array):
        e = exp_translator(e.replace('\n', ''))
        arr.append(e if e else 'None')
    arr = '%s = Js([%s])\n' % (lval, ','.join(arr))
    #But we can have more code to add to define arrays/objects defined inside this array
    # translate nested objects:
    for lval, obj in obj_rep.iteritems():
        new_def, obj_count, arr_count = translate_object(obj, lval, obj_count, arr_count)
        # add object definition BEFORE array definition
        arr = new_def + arr
    for lval, obj in arr_rep.iteritems():
        new_def, obj_count, arr_count = translate_array(obj, lval, obj_count, arr_count)
        # add object definition BEFORE array definition
        arr = new_def + arr
    return arr, obj_count, arr_count



if __name__=='__main__':
    test = 'a = {404:{494:19}}; b = 303; if () {f={:}; {     }}'


    #print remove_objects(test)
    #print list(bracket_split(' {}'))
    print
    print translate_object('{,}', 'ser')[0]


