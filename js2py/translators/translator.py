from flow import translate_flow, indent
from constants import remove_constants, recover_constants
from objects import remove_objects, remove_arrays, translate_object, translate_array

TOP_GLOBAL = '''from pyjs.pyjs import *\nvar = Scope({k:v for k,v in JS_BUILTINS.iteritems()})\n'''

def inject_before_lval(source, lval, code):
    if source.count(lval)>1:
        raise RuntimeError('To many lvals')
    elif not source.count(lval):
        raise RuntimeError('No lval found')
    end = source.index(lval)
    inj = source.rfind('\n', 0, end)
    ind = inj
    while source[ind+1]==' ':
        ind+=1
    ind -= inj
    return source[:inj+1]+ indent(code, ind) + source[inj+1:]

def translate_js(js, top=TOP_GLOBAL):
    """Js has to be a javascript code. Functions and getters/ setters are not supported yet but will be very soon.
        It cant contain with or switch statements.
        Also most of the built in global objects like Number Object RegExp, Math etc
        are not implemented yet"""
    # Remove constant literals
    no_const, constants = remove_constants(js)

    # Remove object literals
    no_obj, objects, obj_count = remove_objects(no_const)

    # Remove arrays
    no_arr, arrays, arr_count = remove_arrays(no_obj)

    # Here remove and replace functions as well
    #todo functions

    #translate flow and expressions
    py_seed, to_register = translate_flow(no_arr)
    register = top + '\n'
    for var in to_register:
        register += 'var.register(%s)\n'% repr(var)
    py_seed = register + py_seed

    #Recover objects
    for obj_lval, obj_code in objects.iteritems():
        translation, obj_count, arr_count = translate_object(obj_code, obj_lval, obj_count, arr_count)
        py_seed = inject_before_lval(py_seed, obj_lval, translation)

    #Recover arrays
    for arr_lval, arr_code in arrays.iteritems():
        translation, obj_count, arr_count = translate_object(arr_code, arr_lval, obj_count, arr_count)
        py_seed = inject_before_lval(py_seed, arr_lval, translation)

    #Recover functions
    #todo functions

    #Recover constants
    py_code = recover_constants(py_seed, constants)

    return py_code


#print inject_before_lval('   chuj\n   moj\n   lval\nelse\n', 'lval', 'siema\njestem piter\n')
import time
print time.time()
print translate_js('if (1) console.log("Hello, World!"); else if (5) console.log("Hello world?");')
print time.time()