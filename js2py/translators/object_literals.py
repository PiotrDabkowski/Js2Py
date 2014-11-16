""" This module has to remove all objects/arrays from JS source code and replace them with LVALS.
Also it has to have a function translating removed object/array to python code.
Code used with this module cant have any function definitions and constants but can contain everything
else."""
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
    return not last or last[-1] in markers or last[-1] not in IDENTIFIER_PART

def remove_objects(code, count=1):
    """ This function replaces objects with OBJECTS_LVALS, returns new code, replacement dict and count.
        count arg is the number that should be added to the LVAL of the first replaced object
    """
    replacements = {'max': count} #replacement dict
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
                replacements['max'] += 1
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
                res += '{%s}' % n
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
    replacements = {'max':count}
    last = ''
    for e in bracket_split(code, ['[]']):
        if e[0]=='[' and is_array(last):
            name = ARRAY_LVAL % count
            res += name
            replacements[name] = e
            count += 1
            replacements['max'] += 1
        else:
            res += e
    return res, replacements


def translate_object(obj, lval, obj_count, arr_count):
    obj, obj_rep, _ = remove_objects(obj, obj_count)
    obj, arr_rep = remove_arrays(obj, arr_count)
    obj_count, arr_count = obj_rep['max'], arr_rep['max']
    obj_code = ''
    for e in argsplit(obj):
        e = e.split(':') # we cant have ; anymore

    return obj, obj_count, arr_count


def translate_gsetter(gsetter):
    pass








def translate_array(array, lval, obj_count, arr_count):
    """array has to be any js array for example [1,2,3]
       lval has to be name of this array.
       Returns python code that adds lval to the PY scope it should be put before lval"""
    array, obj_rep, _ = remove_objects(array, obj_count)
    array, arr_rep = remove_arrays(array, arr_count)
    obj_count, arr_count = obj_rep['max'], arr_rep['max']
    arr = []
    for e in argsplit(array):
        e = exp_translator(e.replace('\n', ''))
        arr.append(e if e else 'None')
    arr = '%s = Js([%s])\n' % (lval, ','.join(e))
    #But we can have more code to add to define arrays/objects defined inside this array
    # translate nested objects:
    for lval, obj in obj_rep.iteritems():
        new_def, obj_count, arr_count = translate_object(obj, lval, obj_count, arr_count)
        # add object definition BEFORE array definition
        arr = new_def + arr
    for lval, obj in obj_rep.iteritems():
        new_def, obj_count, arr_count = translate_array(obj, lval, obj_count, arr_count)
        # add object definition BEFORE array definition
        arr = new_def + arr
    return arr, obj_count, arr_count



test = 'a = {404:{494:19}}; b = 303; if () {f={:}; {     }}'


print remove_objects(test)
print list(bracket_split(' {}'))