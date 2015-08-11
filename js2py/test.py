import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = '''

Array.prototype.max = function(array ){
    return Math.max.apply( Math, array );
};

[1,2,3,4,1,-50, -Infinity].max()
'''

#c.execute(a)
print js2py.eval_js(a)
