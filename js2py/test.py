import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = r'''

a = new Boolean(0)
new String('2') == Number(2)
'''

#c.execute(a)
res = js2py.translate_js(a)
with open('test_res.py', 'wb') as f:
    f.write(res)


def f(a, b, c):
    return [xrange(100),0]

e =  js2py.eval_js("function Test() {return 'Ciera Cola'}"+a)
print e