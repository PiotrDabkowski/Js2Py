<h1><b>Pure Python JavaScript Translator/Interpreter</b></h1>

Translates any valid JavaScript (ECMA Script 5.1) to Python. Translation is fully automatic. Does not have any 
dependencies - uses only standard python library. Still under development. 
<br>
Managed to fully automatically translate esprima to Python - Available <a href="https://github.com/PiotrDabkowski/Js2Py/blob/master/js2py/examples/pyesprima.py"> Here </a>

<hr>
<h1><b>Functionality</b></h1>
Of course translates and evaluates JavaScript code in pure Python:

    >>> from js2py.evaljs import *
    >>> print translate_js('1 + " and 2 is 3"')
    from js2py.pyjs import *
    var = Scope( JS_BUILTINS )
    set_global_object(var)
    (Js(1)+Js(u" and 2 is 3"))
    >>> eval_js('1 + " and 2 is 3"')  
    '1 and 2 is 3'
    >>> f = eval_js('function (a) {return eval(arguments[0]+"*3")}')
    >>> f
    function (a) { [python code] }
    >>> f(10, 100, 1000)
    30

It has few limitations which will be solved in the future:
<ul>
<li>Date and JSON objects are not implemented</li>
<li>Automatic semicolon insertion is not fully implemented yet</li>
<li>RegExp has few bugs</li>
<li>Array prototype is not fully finished</li>
<li>Bitwise operations are not implemented yet</li>
<li>with statement is not supported</li>
<li>Indirect call to eval will is treated as direct call to eval (hence allways evals in local scope)</li>
<li>Invalid JavaScript code may not cause SyntaxError and hence can exhibit unexpected behaviour</li>
</ul>

<hr>
<h1><b>Demo </b></h1>
Let's translate this LongestCommonSubstring algorithm:

    x = '''function lcs(string1, string2){
        	// init max value
        	var longestCommonSubstring = 0;
        	// init 2D array with 0
        	var table = [],
                    len1 = string1.length,
                    len2 = string2.length,
                    row, col;
        	for(row = 0; row <= len1; row++){
        		table[row] = [];
        		for(col = 0; col <= len2; col++){
        			table[row][col] = 0;
        		}
        	}
        	// fill table
                var i, j;
        	for(i = 0; i < len1; i++){
        		for(j = 0; j < len2; j++){
        			if(string1[i]==string2[j]){
        				if(table[i][j] == 0){
        					table[i+1][j+1] = 1;
        				} else {
        					table[i+1][j+1] = table[i][j] + 1;
        				}
        				if(table[i+1][j+1] > longestCommonSubstring){
        					longestCommonSubstring = table[i+1][j+1];
        				}
        			} else {
        				table[i+1][j+1] = 0;
        			}
        		}
        	}
        	return longestCommonSubstring;
        }'''
Here is how to do that:

    >>> from js2py.evaljs import EvalJs
    >>> e = EvalJs()
    >>> e.execute(x) # where x is our longest common subsequence algoritm in JavaScript
    >>> e['lcs']
    function lcs(string1, string2) { [python code] }
    >>> e['lcs']('js2py','pyjs')
    2 
js2py and pyjs have longest common subsequence 'py' which has length 2 so the answer is correct. 

<hr>
<br>
If you are curious this is how the translated code looks like:

    from js2py.pyjs import *
    var = Scope({k:v for k,v in JS_BUILTINS.iteritems()})
    set_global_object(var)
    var.registers(['lcs'])
    @Js
    def PyJsLvalTempHoisted(string1, string2, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'string1':string1, 'string2':string2}, var)
        var.registers(['longestCommonSubstring', 'table', 'len1', 'len2', 'row', 'col', 'i', 'j'])
        var.put('longestCommonSubstring', Js(0))
        PyJsLvalArray1_ = Js([None])
        var.put('table', PyJsLvalArray1_)
        var.put('len1', var.get('string1').get('length'))
        var.put('len2', var.get('string2').get('length'))
        #for JS loop
        var.put('row', Js(0))
        while (var.get('row')<=var.get('len1')):
            PyJsLvalArray2_ = Js([None])
            var.get('table').put(var.get('row'), PyJsLvalArray2_)
            #for JS loop
            var.put('col', Js(0))
            while (var.get('col')<=var.get('len2')):
                var.get('table').get(var.get('row')).put(var.get('col'), Js(0))
                pass
                var.get('col').PostInc()
            
            pass
            var.get('row').PostInc()
        
        pass
        #for JS loop
        var.put('i', Js(0))
        while (var.get('i')<var.get('len1')):
            #for JS loop
            var.put('j', Js(0))
            while (var.get('j')<var.get('len2')):
                if (var.get('string1').get(var.get('i'))==var.get('string2').get(var.get('j'))):
                    if (var.get('table').get(var.get('i')).get(var.get('j'))==Js(0)):
                        var.get('table').get((var.get('i')+Js(1))).put((var.get('j')+Js(1)), Js(1))
                        pass
                    else:
                        var.get('table').get((var.get('i')+Js(1))).put((var.get('j')+Js(1)), (var.get('table').get(var.get('i')).get(var.get('j'))+Js(1)))
                        pass
                    if (var.get('table').get((var.get('i')+Js(1))).get((var.get('j')+Js(1)))>var.get('longestCommonSubstring')):
                        var.put('longestCommonSubstring', var.get('table').get((var.get('i')+Js(1))).get((var.get('j')+Js(1))))
                        pass
                    pass
                else:
                    var.get('table').get((var.get('i')+Js(1))).put((var.get('j')+Js(1)), Js(0))
                    pass
                pass
                var.get('j').PostInc()
            
            pass
            var.get('i').PostInc()
        
        return var.get('longestCommonSubstring')
        pass
        pass
    PyJsLvalTempHoisted.func_name = 'lcs'
    var.put('lcs', PyJsLvalTempHoisted)
    pass


It's ugly mostly because of this var thing which is a scope variable but it was necessary in order to implement JavaScript closures and non legel in Python identifier names like $.

