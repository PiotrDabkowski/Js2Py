####Pure Python JavaScript Translator/Interpreter

Translates any valid JavaScript (ECMA Script 5.1) to Python. Translation is fully automatic. Does not have any 
dependencies - uses only standard python library. Still under development. 
<hr>

Managed to fully automatically translate esprima to Python! - Available <a href="https://github.com/PiotrDabkowski/Js2Py/blob/master/examples/pyesprima.py"> Here </a>

<hr>
####Functionality
Of course translates and evaluates JavaScript code in pure Python:

    >>> import js2py
    >>> f = js2py.eval_js( "function (a) {return a + arguments[1]}" )
    >>> f
    function (a) { [python code] }
    >>> f(1, 2, 3)
    3

<hr>

What's more Js2Py also supports importing any Python code from JavaScript using 'pyimport' statement:

    >>> x = """pyimport urllib;
               var result = urllib.urlopen('https://www.google.com/').read();
               console.log(result.length)
            """
    >>> js2py.eval_js(x)
    18211
    undefined
    
It has few limitations which will be solved in the future:
<ul>
<li>Date and JSON objects are not implemented</li>
<li>RegExp has few bugs</li>
<li>Array prototype is not fully finished</li>
<li>Bitwise operations are not implemented yet</li>
<li>with statement is not supported</li>
<li>Indirect call to eval will is treated as direct call to eval (hence always evals in local scope)</li>
<li>Invalid JavaScript code may not cause SyntaxError and hence can exhibit unexpected behaviour</li>
</ul>

You can help me to fix these problems if you want since I don't have time to do that. Js2Py would be complete :)
In the future I will maybe replace my home made JS parser with Esprima because Esprima is much more reliable (but also slower). 

<b> Automatic semicolon insertion is supported! </b>

<hr>
####Demo
Let's translate this Longest Common Substring algorithm:

    x = """function lcs(a, b) {
        var m = a.length, n = b.length,
            C = [], i, j;
        for (i = 0; i <= m; i++) C.push([0]);
        for (j = 0; j < n; j++) C[0].push(0);
        for (i = 0; i < m; i++)
            for (j = 0; j < n; j++)
                C[i+1][j+1] = a[i] === b[j] ? C[i][j]+1 : Math.max(C[i+1][j], C[i][j+1]);
        return (function bt(i, j) {
            if (i*j === 0) { return ""; }
            if (a[i-1] === b[j-1]) { return bt(i-1, j-1) + a[i-1]; }
            return (C[i][j-1] > C[i-1][j]) ? bt(i, j-1) : bt(i-1, j);
        }(m, n));
        }"""
        
Here is how to do that:

    >>> from js2py import EvalJs
    >>> j = EvalJs()
    >>> j.execute(x) # where x is our longest common subsequence algoritm in JavaScript above
    >>> j.lcs        # accessing translated function
    function lcs(string1, string2) { [python code] }
    >>> j.lcs('website','webmaster')
    'webste'
As you can see js2py can fully automatically translate advanced javascript code. 


    
<hr>
<br>
If you are curious this is how the translated code looks like:

    >>> print js2py.translate_js(x)
    from js2py.pyjs import *
    var = Scope( JS_BUILTINS )
    set_global_object(var)
    var.registers([u'lcs'])
    @Js
    def PyJsLvalTempHoisted(a, b, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, u'a':a, u'b':b}, var)
        var.registers([u'm', u'n', u'C', u'i', u'j'])
        var.put(u'm', var.get(u'a').get(u'length'))
        var.put(u'n', var.get(u'b').get(u'length'))
        PyJsLvalArray1_ = Js([None])
        var.put(u'C', PyJsLvalArray1_)
        #for JS loop
        var.put(u'i', Js(0))
        while (var.get(u'i')<=var.get(u'm')):
            PyJsLvalArray2_ = Js([Js(0)])
            var.get(u'C').callprop(u'push',PyJsLvalArray2_)
            var.get(u'i').PostInc()
        
        #for JS loop
        var.put(u'j', Js(0))
        while (var.get(u'j')<var.get(u'n')):
            var.get(u'C').get(Js(0)).callprop(u'push',Js(0))
            var.get(u'j').PostInc()
        
        #for JS loop
        var.put(u'i', Js(0))
        while (var.get(u'i')<var.get(u'm')):
            #for JS loop
            var.put(u'j', Js(0))
            while (var.get(u'j')<var.get(u'n')):
                var.get(u'C').get((var.get(u'i')+Js(1))).put((var.get(u'j')+Js(1)), ((var.get(u'C').get(var.get(u'i')).get(var.get(u'j'))+Js(1)) if var.get(u'C').get((var.get(u'i')+Js(1))).put((var.get(u'j')+Js(1)), PyJsStrictEq(var.get(u'a').get(var.get(u'i')),var.get(u'b').get(var.get(u'j')))) else var.get(u'Math').callprop(u'max',var.get(u'C').get((var.get(u'i')+Js(1))).get(var.get(u'j')),var.get(u'C').get(var.get(u'i')).get((var.get(u'j')+Js(1))))))
                var.get(u'j').PostInc()
            
            var.get(u'i').PostInc()
        
        @Js
        def PyJsLvalInline1_(i, j, this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments, u'i':i, u'j':j, u'bt':PyJsLvalInline1_}, var)
            if PyJsStrictEq((var.get(u'i')*var.get(u'j')),Js(0)):
                return Js(u"")
                pass
            if PyJsStrictEq(var.get(u'a').get((var.get(u'i')-Js(1))),var.get(u'b').get((var.get(u'j')-Js(1)))):
                return (var.get(u'bt')((var.get(u'i')-Js(1)),(var.get(u'j')-Js(1)))+var.get(u'a').get((var.get(u'i')-Js(1))))
                pass
            return (var.get(u'bt')(var.get(u'i'),(var.get(u'j')-Js(1))) if ((var.get(u'C').get(var.get(u'i')).get((var.get(u'j')-Js(1)))>var.get(u'C').get((var.get(u'i')-Js(1))).get(var.get(u'j')))) else var.get(u'bt')((var.get(u'i')-Js(1)),var.get(u'j')))
            pass
            pass
        return (PyJsLvalInline1_(var.get(u'm'),var.get(u'n')))
        pass
        pass
    PyJsLvalTempHoisted.func_name = u'lcs'
    
    var.put(u'lcs', PyJsLvalTempHoisted)
    pass


It's ugly mostly because of this var thing which is a scope variable but it was necessary in order to implement JavaScript closures and non legel in Python identifier names like $.

