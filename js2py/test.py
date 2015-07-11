import js2py

js = 'function k(){return 9}'
e = js2py.eval_js(js).to_python()
print e
