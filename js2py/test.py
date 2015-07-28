import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = """

f = 554
a = {set s(val) {f = val}, get s() {return f}}

l = [3,5,0]
l[2] = l
a.b = l
a.d = a
console.log(a)

"""
#c.execute(a)
#print c.console()
print js2py.eval_js(a)