import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = r'''

b = {88:99}
a = [0,1,2]
a[1] = b
b[9000] = a
JSON.stringify(b)
'''

#c.execute(a)
res = js2py.translate_js(a)
with open('test_res.py', 'wb') as f:
    f.write(res)


def f(a, b, c):
    return [xrange(100),0]

e =  js2py.eval_js("function test() {return 'Ciera Cola'}"+a)
print e