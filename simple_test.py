import js2py
import time
import sys

sys.setrecursionlimit(10000)

print("Testing ECMA 5...")


assert js2py.eval_js('(new Date("2008-9-03T20:56:35.450686Z")).toString()')

assert js2py.eval_js('/ser/.test("Mleko + ser to nabial")')
assert js2py.eval_js('1 + "1"') == '11'

assert js2py.eval_js('function (r) {return r}')(5) == 5

x, c = js2py.run_file('examples/esprima.js')
assert c.esprima.parse('var abc = 40').to_dict() == {'type': 'Program', 'body': [{'type': 'VariableDeclaration', 'kind': 'var', 'declarations': [{'id': {'type': 'Identifier', 'name': 'abc'}, 'type': 'VariableDeclarator', 'init': {'type': 'Literal', 'raw': '40', 'value': 40}}]}], 'sourceType': 'script'}
assert js2py.eval_js('var x = {get y() { return this.val;}, val: 11};x.y') == 11
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


# Simple PyWrapper test
class Foo:
    def __init__(self, bar):
        self.bar = bar
        self.bar_history = []

    def set_bar(self, x):
        import copy
        self.bar_history.append(copy.deepcopy(self))
        self.bar = x

    def get_bar(self):
        return self.bar

pyobj = Foo(5)
context = js2py.EvalJs({'foo': pyobj})
assert context.foo.bar == 5
context.execute('foo.bar = 7')
assert context.foo.bar == 7
context.execute('foo.bar += 15.22')
assert context.foo.bar == 22.22
context.execute('foo.bar /= 2')
assert context.foo.bar == 11.11
assert pyobj.bar == 11.11
context.execute('foo.set_bar(foo.get_bar())')
assert context.foo.get_bar() == 11.11
context.execute('foo.set_bar(33)')
assert context.foo.get_bar() == 33
assert context.eval('foo.bar_history.push(foo.bar_history[1].get_bar());foo.bar_history[foo.bar_history.length-1].get_bar()') == 11.11

print("Passed ECMA 5 simple tests!\n"+30*'-')

print('Now harder tests - test on huge JS libraries:')

# crypto-js ( https://www.npmjs.com/package/crypto-js )
print('Testing crypto-js')
CryptoJS = js2py.require('crypto-js@3.1.8')
data = [{'id': 1}, {'id': 2}]
JSON = js2py.eval_js('JSON')
ciphertext = CryptoJS.AES.encrypt(JSON.stringify(data), 'secret key 123')
bytes  = CryptoJS.AES.decrypt(ciphertext.toString(), 'secret key 123')
decryptedData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8)).to_list()
assert decryptedData == data

AES = js2py.require('crypto-js/aes@3.1.8')
ciphertext = AES.encrypt(JSON.stringify(data), 'secret key 123')
bytes  = AES.decrypt(ciphertext.toString(), 'secret key 123')
decryptedData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8)).to_list()
assert decryptedData == data


# esprima ( https://www.npmjs.com/package/esprima )
# escodegen ( https://github.com/estools/escodegen )
print('Testing esprima & escodegen')
esprima = js2py.require('esprima')
escodegen = js2py.require('escodegen')
print('now use the translated esprima to parse some js code!')
sample_js_code = '''
function helloWorld(a, b, c) {
     console.log(this+a+b+c); 8; var x={hh:1,i:0};
     if (a!=1) {
        return x
     } else {
        throw error
     }
}
'''
# we can even parse esprima's own source code, but its size is too big for the travis test.
#sample_js_code = js2py.get_file_contents('examples/esprima.js')
parsed = esprima.parse(sample_js_code)
print('use escodegen to get back the js code from the parsed AST')
reconstructed = escodegen.generate(parsed)
parsed2 = esprima.parse(sample_js_code)
reconstructed2 = escodegen.generate(parsed)
assert reconstructed==reconstructed2 and len(reconstructed)>=len(sample_js_code)


# chalk ( https://github.com/chalk/chalk )
# print('For the final test use chalk. this is interesting because it '
#       'uses ES6 objects like Map, Therefore we have to include the polyfills!')
# chalk = js2py.require('chalk', include_polyfill=True)
# chalk = chalk.constructor.new({'level': 2})
# true_text = '\x1b[34mHello \x1b[4m\x1b[44mworld\x1b[49m\x1b[24m!\x1b[39m'
# text = chalk.blue('Hello', chalk.underline.bgBlue('world') + '!')
# print(text)
# assert text==true_text

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


from js2py.internals import seval
assert seval.eval_js_vm("function k() {try {throw 3+8} catch (e) {console.log(e);return e}};k()", debug=True) == 11.0