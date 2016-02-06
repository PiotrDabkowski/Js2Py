import js2py



print(js2py.eval_js(''' JSON.stringify(  [ ,, new Date() ,,,,]  );

    '''))


print(js2py.eval_js("Object.prototype.toString.call(Function('s', 'return s+arguments[1]')(new Date(), 7).__proto__)"))


print(js2py.eval_js(''' '14'/'3'

    '''))

js2py.EvalJs().console()


