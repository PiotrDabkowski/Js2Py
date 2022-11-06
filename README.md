[![Build Status](https://travis-ci.org/PiotrDabkowski/Js2Py.svg?branch=master)](https://travis-ci.org/PiotrDabkowski/Js2Py) [![Downloads](https://pepy.tech/badge/js2py/month)](https://pepy.tech/project/js2py)

#### Pure Python JavaScript Translator/Interpreter

Everything is done in 100% pure Python so it's extremely easy to install and use. Supports Python 2 & 3. Full support for ECMAScript 5.1, ECMA 6 support is still experimental.
<hr>

Simple Example:

```python
    >>> import js2py
    >>> js2py.eval_js('console.log( "Hello World!" )')
    'Hello World!'
    >>> add = js2py.eval_js('function add(a, b) {return a + b}')
    >>> add(1, 2) + 3
    6
    >>> add.constructor
    function Function() { [python code] }
    >>> js2py.require('underscore')
    'function _(obj) { [python code] }'
```
You can also import a big number of node modules as if they were written in Python!
For example, here we import a pure JS library [crypto-js](https://www.npmjs.com/package/crypto-js):

```python
    >>> CryptoJS = js2py.require('crypto-js')
    >>> data = [{'id': 1}, {'id': 2}]
    >>> JSON = js2py.eval_js('JSON')
    >>> ciphertext = CryptoJS.AES.encrypt(JSON.stringify(data), 'secret key 123')
    >>> bytes  = CryptoJS.AES.decrypt(ciphertext.toString(), 'secret key 123')
    >>> decryptedData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8)).to_list()
    >>> decryptedData
    [{u'id': 1}, {u'id': 2}]
```



Now also supports JavaScript 6 (still experimental):

```python
    >>> js2py.eval_js6('let a = () => 11; a()')
    11
```
JavaScript 6 support was achieved by using Js2Py to translate javascript library called <a href="https://github.com/babel/babel">Babel</a>. Babel translates JS 6 to JS 5 and afterwards Js2Py translates JS 5 to Python. The only downside is that translated babel.js has about 4 MB and importing such a long Python file takes about 15 seconds!

<hr>

Translating a JavaScript file:

```python
    # this will translate example.js to example.py
    >>> js2py.translate_file('example.js', 'example.py')
    # example.py can be now imported and used!
    >>> from example import example
    >>> example.someFunction()
    ...
```
   
Every feature of ECMA 5.1 is implemented (except of 'with' statement):

```python
>>> js2py.eval_js("Object.prototype.toString.call(Function('s', 'return s+arguments[1]')(new Date(), 7).__proto__)")
[object String]
```
Unfortunately even though Js2Py can be generally used to translate huge Js files (over 50k lines long), in rare cases you may encounter some unexpected problems (like javascript calling a function with 300 arguments - python allows only 255). These problems are very hard to fix with current translation approach. I will try to implement an interpreter in near future which will hopefully fix all the edge cases.

#### Installation 

    pip install js2py
    
<hr>

#### More advanced usage example

It is possible to access all the variables from JS scope using EvalJs. Moreover, you can use Python objects from your JavaScript code if you add them to the scope. 
In this example we will be using Python built-in sum function to sum elements in JS array. It will stand under python_sum.

```python
# Adding Python built-in sum to the JS context:
>>> context = js2py.EvalJs({'python_sum': sum})  
>>> js_code = '''
var a = 10
function f(x) {return x*x}
'''
>>> context.execute(js_code)
# Get value of variable a:
>>> context.a
10
# context.f behaves just like js function so you can supply more than 1 argument. '9'*'9' in javascript is 81.
>>> context.f('9', 0)  
81    
# context.f has all attributes of normal JavaScript object
>>> context.f.toString()
u'function f(x) { [python code] }'
>>> context.f.bind
function bind(thisArg) { [python code] }
# You can also add variables to the context:
>>> context.foo = [1,2,3]  # context.foo is now Js Array object and behaves just like javascript array!
>>> context.foo.push(4)  
4
>>> context.foo.to_list() # convert to python list
[1, 2, 3, 4]
# You can use Python objects that you put inside the context!
>>> context.eval('python_sum(new Array(1, 2, 3))')
6
 ```   

You can also enable require support in JavaScript like this:

```python
>>> context = js2py.EvalJs(enable_require=True)
>>> context.eval("require('esprima').parse('var a = 1')")
```
<hr>

### JavaScript 'VirtualMachine' in Python

As a fun experimental project I have also implemented a VM-based JavaScript 
(yes - there are 2 separate JS implementations in this repo). It is feature complete and faster than the translation based version.
Below you can see a demo with a nice debug view (bytecode + execution sequence):

```python
>>> from js2py.internals import seval
>>> seval.eval_js_vm("try {throw 3+3} catch (e) {console.log(e)}", debug=True)
[LOAD_UNDEFINED(),
 JUMP(4,),
 LABEL(1,),
 LOAD_UNDEFINED(),
 POP(),
 LOAD_NUMBER(3.0,),
 LOAD_NUMBER(3.0,),
 BINARY_OP('+',),
 THROW(),
 NOP(),
 LABEL(2,),
 LOAD_UNDEFINED(),
 POP(),
 LOAD('console',),
 LOAD('e',),
 LOAD_N_TUPLE(1,),
 CALL_METHOD_DOT('log',),
 NOP(),
 LABEL(3,),
 LOAD_UNDEFINED(),
 NOP(),
 LABEL(4,),
 TRY_CATCH_FINALLY(1, 2, 'e', 3, False, 4)]

0 LOAD_UNDEFINED()
1 JUMP(4,)
18 TRY_CATCH_FINALLY(1, 2, 'e', 3, False, 4)
  ctx entry (from:2, to:9)
  2 LOAD_UNDEFINED()
  3 POP()
  4 LOAD_NUMBER(3.0,)
  5 LOAD_NUMBER(3.0,)
  6 BINARY_OP('+',)
  7 THROW()
  ctx exit (js errors)
  ctx entry (from:9, to:16)
  9 LOAD_UNDEFINED()
  10 POP()
  11 LOAD('console',)
  12 LOAD('e',)
  13 LOAD_N_TUPLE(1,)
  14 CALL_METHOD_DOT('log',)
6
  15 NOP()
  ctx exit (normal)

```

This is just a curiosity and I do not recommend using VM in practice (requires more polishing).
 
<hr>

#### Limitations

There are 3 main limitations:
<ul>
<li>"strict mode" is ignored</li>
<li>with statement is not supported</li>
<li>Indirect call to eval is treated as direct call to eval (hence always evals in local scope)</li>
</ul>

They are generally not a big issue in practice.
In practice more problematic are minor edge cases that unfortunately
sometimes do happen. Please report a bug if you find one. 

Js2Py was able to successfully 
translate and run huge JS libraries like Babel (100k+ loc), esprima, crypto-js and more.
You can try it yourself by importing any supported npm package via `js2py.require('your_package')`.

<hr>



#### Other Examples


In Js2Py all JavaScript objects are a subclass of PyJs object. For example JS Number is represented by PyJsNumber class.
js2py.eval_js and js2py.EvalJs automatically tries to convert PyJs type to builtin python type. So for example if you 
execute:

```python
>>> js2py.eval_js('var a = "hello"; a')
```

eval_js will return unicode type (u"hello"). However for complex types such conversion is impossible and JsObjectWrapper is returned.
See the conversion table JsType -> PyType:

    Boolean -> bool
    String -> unicode (str in Python 3)
    Number -> float (or int/long if whole number)
    undefined -> None
    null -> None
    OTHER -> JsObjectWrapper

JsObjectWrapper supports: getitem, getattr, setitem, setattr, repr and call.
Moreover it has to_list and to_dict methods if you want to convert it to builtin python type.

```python
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
{a: 1, b: 20}  
>>> js['c'] = 30
>>> js.to_dict()
{u'a': 1, 'c': 30, u'b': 20}
```

<hr>

Also, of course you can use Js2Py to parse (tree is the same as in esprima.js) and translate JavaScript

#### Parsing:
```python
>>> js2py.parse_js('var $ = 5')   
{
    "body": [
        {
            "declarations": [
                {
                    "id": {
                        "name": "$",
                        "type": "Identifier"
                    },
                    "init": {
                        "raw": "5",
                        "type": "Literal",
                        "value": 5
                    },
                    "type": "VariableDeclarator"
                }
            ],
            "kind": "var",
            "type": "VariableDeclaration"
        }
    ],
    "type": "Program"
}
```
#### Translating:

```python
>>> print(js2py.translate_js('var $ = 5'))
from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['$'])
var.put('$', Js(5.0))
 ```
<hr>

#### pyimport statement
Finally, Js2Py also supports importing any Python code from JavaScript using 'pyimport' statement:

```python
>>> x = """pyimport urllib;
           var result = urllib.urlopen('https://www.google.com/').read();
           console.log(result.length)
        """
>>> js2py.eval_js(x)
18211
undefined
```


    
