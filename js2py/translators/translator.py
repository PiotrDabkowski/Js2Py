from flow import translate_flow, indent
from constants import remove_constants, recover_constants
from objects import remove_objects, remove_arrays, translate_object, translate_array, set_func_translator
from functions import remove_functions, reset_inline_count


TOP_GLOBAL = '''from pyjs.pyjs import *\nvar = Scope({k:v for k,v in JS_BUILTINS.iteritems()})\n'''

def inject_before_lval(source, lval, code):
    if source.count(lval)>1:
        print source
        print lval
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

    # Here remove and replace functions
    reset_inline_count()
    no_func, hoisted, inline = remove_functions(no_arr)

    #translate flow and expressions
    py_seed, to_register = translate_flow(no_func)

    # register variables and hoisted functions
    #top += '# register variables\n'
    top += 'var.registers(%s)\n' % str(to_register + hoisted.keys())

    #Recover functions
    # hoisted functions recovery
    defs = ''
    #defs += '# define hoisted functions\n'
    for nested_name, nested_info in hoisted.iteritems():
        nested_block, nested_args = nested_info
        new_code = translate_func(nested_name, nested_block, nested_args)
        top += new_code +'\n'
    #defs += '# Everting ready!\n'
    # inline functions recovery
    for nested_name, nested_info in inline.iteritems():
        nested_block, nested_args = nested_info
        new_code = translate_func(nested_name, nested_block, nested_args)
        py_seed = inject_before_lval(py_seed, nested_name, new_code)
    # add hoisted definitiond - they have literals that have to be recovered
    py_seed = defs + py_seed

    #Recover arrays
    for arr_lval, arr_code in arrays.iteritems():
        translation, obj_count, arr_count = translate_array(arr_code, arr_lval, obj_count, arr_count)
        py_seed = inject_before_lval(py_seed, arr_lval, translation)

    #Recover objects
    for obj_lval, obj_code in objects.iteritems():
        translation, obj_count, arr_count = translate_object(obj_code, obj_lval, obj_count, arr_count)
        py_seed = inject_before_lval(py_seed, obj_lval, translation)


    #Recover constants
    py_code = recover_constants(py_seed, constants)

    return top + py_code

def translate_func(name, block, args):
    """Translates functions and all nested functions to Python code.
       name -  name of that function (global functions will be available under var while
            inline will be available directly under this name )
       block - code of the function (*with* brackets {} )
       args - arguments that this function takes"""
    inline = name.startswith('PyJsLvalInline')
    arglist = ', '.join(args) +', ' if args else ''
    code = '@Js\ndef %s(%sthis, arguments):\n' % (name, arglist)
    # register local variables
    scope = "'this':this, 'arguments':arguments" #it will be a simple dictionary
    for arg in args:
        scope += ', %s:%s' %(repr(arg), arg)
    code += indent('var = Scope({%s}, var)\n' % scope)
    block, nested_hoisted, nested_inline = remove_functions(block)
    py_code, to_register = translate_flow(block)
    #register variables declared with var and names of hoisted functions.
    to_register += nested_hoisted.keys()
    if to_register:
        code += indent('var.registers(%s)\n'% str(to_register))
    for nested_name, info in nested_hoisted.iteritems():
        nested_block, nested_args = info
        new_code = translate_func(nested_name, nested_block, nested_args)
        # Now put definition of hoisted function on the top
        code += indent(new_code)
    for nested_name, info in nested_inline.iteritems():
        nested_block, nested_args = info
        new_code = translate_func(nested_name, nested_block, nested_args)
        # Inject definitions of inline functions just before usage
        py_code = inject_before_lval(py_code, nested_name, new_code)
    if py_code.strip():
        code += indent(py_code)
    return code

set_func_translator(translate_func)


#print inject_before_lval('   chuj\n   moj\n   lval\nelse\n', 'lval', 'siema\njestem piter\n')
import time
#print time.time()
#print translate_js('if (1) console.log("Hello, World!"); else if (5) console.log("Hello world?");')
#print time.time()
t = """
// Both setters and getters work
var object = {element1: 1, element2: 2, set x(val) {this.x = val;}};

for (var element in array) {
  console.log(element);
}

// ?: expression too
var result = Math.random() < 0.3 ? 'Less than 0.3' : 'More than 0.3';

// functions of course
var func = function (a, b, c) {
  if (a + b === c)
    console.log("Hello, World!");
  else if (Something) {
    var y = 109<<30, z = 8 + "hey";
    console.log( z );
  }
   else
     return function () {console.log("Else");};
}, n = 0;

//loops
do {
   var def = n += 1;
   n++;
   ++n;
} while ( n < 100 )

}
"""

print translate_js(t)