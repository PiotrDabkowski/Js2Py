import js2py


print js2py.eval_js('(new Date()).toString()')
print js2py.eval_js('(new Date(0)).toString()')
print js2py.eval_js('(new Date("2008-9-03T20:56:35.450686Z")).toString()')

x, c = js2py.run_file('examples/esprima.js')
assert c.esprima.parse('var abc = 40').to_dict() == {'type': 'Program', 'body': [{'type': 'VariableDeclaration', 'kind': 'var', 'declarations': [{'id': {'type': 'Identifier', 'name': 'abc'}, 'type': 'VariableDeclarator', 'init': {'type': 'Literal', 'raw': '40', 'value': 40}}]}], 'sourceType': 'script'}

assert js2py.eval_js('/ser/.test("Mleko + ser to nabial")')
assert js2py.eval_js('1 + "1"') == '11'


