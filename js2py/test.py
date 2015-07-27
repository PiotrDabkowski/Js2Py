import js2py
c = js2py.EvalJs()
c.execute('a = {d:4,f:function k() {return 1}}')
c.execute('function k(a) {console.log(a);console.log(this)}')
c.execute('f = function (){}')
c.execute('g=function g(){}')
c.console()