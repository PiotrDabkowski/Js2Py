import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = '''
assert = console.log
var test = function () {
    //private members
    var x = 1;
    var y = function () {
        return x * 2;
    };
    //public interface
    return {
        setx : function (newx) {
            x = newx;
        },
        gety : function () {
            return y();
        }
    }
}();

assert(undefined == test.x);
assert(undefined == test.y);
assert(2 == test.gety());
test.setx(5);
assert(10 == test.gety());
'''

#c.execute(a)
print js2py.translate_js(a)
