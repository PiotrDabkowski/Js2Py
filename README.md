####Pure Python JavaScript Translator/Interpreter

Translates any valid JavaScript (ECMA Script 5.1) to Python. Translation is fully automatic. Does not have any 
dependencies - <b>uses only standard python library.</b>
<hr>

Managed to fully automatically translate esprima to Python! - Available <a href="https://github.com/PiotrDabkowski/Js2Py/blob/master/examples/pyesprima.py"> Here </a>

<hr>
####Functionality

<ul>
<li>Automatically translates JavaScript to Python - Supports virtually everything (see limitations)</li>
<li>Supports importing Python libraries from JavaScript code using pyimport statement</li>
<li>Very fast JavaScript Parsing - can be used as standalone JS parser, syntax tree is just like in esprima.js (use js2py.parse_js) </li>
<li> Provides friendly JS execution features - js2py.eval_js for single execution and js2py.EvalJs for continuous </li>
</ul>


Simple Example:

    >>> import js2py
    >>> add = js2py.eval_js('function add(a, b) {return a + b}')
    >>> add(1, 2) + 3
    6
    >>> add('1', 2, 3) 
    u'12'
    >>> add.constructor
    function Function() { [python code] }
    
    >>> js = EvalJs()
    >>> js.execute('var a = 10;function f(x) {return x*x};')
    >>> js.f(9)
    81
    >>> js.a
    10

<hr>

####Limitations

It has few limitations which will be solved in the future:
<ul>
<li>Date and JSON objects are not implemented</li>
<li>with statement is not supported</li>
<li>Indirect call to eval will is treated as direct call to eval (hence always evals in local scope)</li>
</ul>

You can help me to fix these problems if you want.


<hr>

####Installation 

    pip install js2py
    
<hr>

####Other Examples


In Js2Py all JavaScript objects are a subclass of PyJs object. For example JS Number is represented by PyJsNumber class.
js2py.eval_js and js2py.EvalJs automatically tries to convert PyJs type to builtin python type. So for example if you 
execute:

>>> js2py.eval_js('"hello"')

you will get unicode type. However for complex types such conversion is impossoble and JsObjectWrapper
See the conversion table JsType -> PyType:

    Boolean -> bool
    String -> unicode
    Number -> float (or int/long if whole number)
    undefined -> None
    null -> None
    OTHER -> JsObjectWrapper

JsObjectWrapper supports: getitem, getattr, setitem, setattr, repr and call.
Moreover it has to_list and to_dict methods if you want to convert it to builtin python type.

    >>> js = js2py.eval_js('d = {a:1, b:2}')
    >>> js
    {a: 1, b: 2}  
    >>> type(js)
    <class 'js2py.base.JsObjectWrapper'>
    >>> js.a
    1
    >>> js['a']
    1
    >>> js.b = 20
    >>> js
    {a: 1, b: 2}  
    >>> js['c'] = 30
    >>> js.to_dict()
    {u'a': 1, 'c': 30, u'b': 20}


<hr>

Also, of course you can use Js2Py to parse (tree is the same as in esprima.js) and translate JavaScript

#Parsing:

    >>> js2py.parse_js('var $ = 5')   
    {'body': [{'kind': 'var', 'declarations': [{'init': {'raw': None, 'type': u'Literal', 'value': 5.0}, 'type': u'VariableDeclarator', 'id': {'type': u'Identifier', 'name': u'$'}}], 'type': u'VariableDeclaration'}], 'type': u'Program'}

#Transating:

    >>> print js2py.translate_js('var $ = 5')
    import js2py.pyjs, sys
    # Redefine builtin objects... Do you have a better idea?
    for m in sys.modules.keys():
        if m.startswith('js2py'):
            del sys.modules[m]
    del js2py.pyjs
    del js2py
    from js2py.pyjs import *
    # setting scope
    var = Scope( JS_BUILTINS )
    set_global_object(var)
    
    # Code follows:
    var.registers([u'$'])
    var.put(u'$', Js(5.0))
    
<hr>

#pyimport statement
Finally, Js2Py also supports importing any Python code from JavaScript using 'pyimport' statement:

    >>> x = """pyimport urllib;
               var result = urllib.urlopen('https://www.google.com/').read();
               console.log(result.length)
            """
    >>> js2py.eval_js(x)
    18211
    undefined
    


    
