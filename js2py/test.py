import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = r'''
function testcase() {
  var o = {};

  // create a data valued property; all other attributes default to false.
  var d1 = { value: 101 };
  Object.defineProperty(o, "foo", d1);

  // now, trying to change the value of "foo" should fail, since both
  // [[Configurable]] and [[Writable]] on the original property will be false.
  var desc = { value: 102 };

  try {
    Object.defineProperty(o, "foo", desc);
    console.log(o.foo)

  }
  catch (e) {
    if (e instanceof TypeError) {
      // the property should remain unchanged.
      var d2 = Object.getOwnPropertyDescriptor(o, "foo");

      if (d2.value === 101 &&
          d2.writable === false &&
          d2.enumerable === false &&
          d2.configurable === false) {
        return true;
      }
    }
  }
 }

 testcase()
'''

#c.execute(a)
res = js2py.translate_js(a)
with open('test_res.py', 'wb') as f:
    f.write(res)

print js2py.eval_js(a)

