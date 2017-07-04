import js2py
import time

print("Testing ECMA 5...")
assert js2py.eval_js('(new Date("2008-9-03T20:56:35.450686Z")).toString()')

assert js2py.eval_js('/ser/.test("Mleko + ser to nabial")')
assert js2py.eval_js('1 + "1"') == '11'

assert js2py.eval_js('function (r) {return r}')(5) == 5

x, c = js2py.run_file('examples/esprima.js')
assert c.esprima.parse('var abc = 40').to_dict() == {'type': 'Program', 'body': [{'type': 'VariableDeclaration', 'kind': 'var', 'declarations': [{'id': {'type': 'Identifier', 'name': 'abc'}, 'type': 'VariableDeclarator', 'init': {'type': 'Literal', 'raw': '40', 'value': 40}}]}], 'sourceType': 'script'}

try:
    assert js2py.eval_js('syntax error!') and 0
except js2py.PyJsException as err:
    assert str(err).startswith('SyntaxError: ')


assert js2py.eval_js('pyimport time; time.time()') <= time.time()

js2py.disable_pyimport()
try:
    assert js2py.eval_js('pyimport time') and 0
except js2py.PyJsException as err:
    assert str(err).startswith('SyntaxError: ')

print("Passed ECMA 5!\n"+30*'-')

print("Testing ECMA 6...")

assert js2py.eval_js6('''
const v = 11;
obj = {value: v};
obj.x = function() {
    return () => this
};

// since arrow functions remember scope this should return obj.
obj.x()()
''').value == 11

assert js2py.eval_js6('''
var x;
for (let a of [1,2,3]) {
    console.log(a);
    x = a
}

typeof a === 'undefined' && x === 3
''')

assert js2py.eval_js6('''
class Shape {
    constructor (id, x, y) {
        this.id = id
        this.move(x, y)
    }
    move (x, y) {
        this.x = x
        this.y = y
    }
};

a = new Shape(1,2,3)
''').x == 2
print("Passed ECMA 6!")

