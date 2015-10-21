import js2py


a = r'''

function runTestCase(testcase) {
    if (testcase() !== true) {
        $ERROR("Test case returned non-true value!");
    }
}


function testcase() {
  var s = new String("hello world");
  s.foo = 2;

  if (s["foo"] === 1) {
    return true;
  }
 }
runTestCase(testcase);


'''


res = js2py.translate_js(a)
with open('test_res.py', 'wb') as f:
    f.write(res)

e = js2py.eval_js(a)
print e