# coding=utf-8
""" This module is still experimental! It has a lot of bugs and host/constructor objects are not implemented yet.
"""

from translators.translator import translate_js, dbg


class EvalJs(object):
    def __init__(self, context=None):
        self.context = {}
        self.__started = False

    def execute(self, js):
        """executes javascript js in current context"""
        js = js.replace('\t', '\n')  # have to remove tabs in parser 
        if not self.__started:
            code = translate_js(js)
            self.__started = True
        else:
            code = translate_js(js, '')
        dbg(code)
        print code
        exec code in self.context

    def __getattr__(self, var):
        return self.get_variable(var)

    def get_variable(self, var):
        """returns variable from global JS context"""
        return self.context['var'].get(var)

    def __getitem__(self, var):
        return self.get_variable(var)


x = ur'''

//"no strict";
var strict_mode = false;
var NotEarlyErrorString = "NotEarlyError";
var EarlyErrorRePat = "^((?!" + NotEarlyErrorString + ").)*$";
var NotEarlyError = new Error(NotEarlyErrorString);

function Test262Error(message) {
    this.message = message || "";
}

Test262Error.prototype.toString = function () {
    return "Test262Error: " + this.message;
};

var $ERROR;
$ERROR = function $ERROR(message) {
    throw new Test262Error(message);
};

function testFailed(message) {
    $ERROR(message);
}

function testRun(id, path, description, codeString, result, error) {
  if (result!=="pass") {
      throw new Error("Test '" + path + "'failed: " + error);
  }
}

// define a default `print` function for async tests where there is no
// global `print`
var print;

// in node use console.log
if (typeof console === "object") {
    print = function () {
        var args = Array.prototype.slice.call(arguments);
        console.log(args.join(" "));
    };
}

// in WScript, use WScript.Echo
if (typeof WScript === "object") {
    print = function () {
        var args = Array.prototype.slice.call(arguments);
        WScript.Echo(args.join(" "));
    };

    // also override $ERROR to force a nonzero exit code exit
    // TODO? report syntax errors
    var oldError = $ERROR;
    $ERROR = function (message) {
        print("Test262 Error: " + message);
        WScript.Quit(1);
    };
}

function runTestCase(testcase) {
    if (testcase() !== true) {
        $ERROR("Test case returned non-true value!");
    }
}

function testcase() {
        var tokenCodes  = {};
        tokenCodes.continue = 0;
        tokenCodes.for = 1;
        tokenCodes.switch = 2;
        var arr = [
            'continue',
            'for',
            'switch'
        ];
        for(var p in tokenCodes) {
            for(var p1 in arr) {
                if(arr[p1] === p) {
                    console.log(tokenCodes);
                    console.log(arr[p1]);
                    if(!tokenCodes.hasOwnProperty(arr[p1])) {
                        return false;
                    };
                }
            }
        }
        console.log('hehehehehehehehehe');
        return true;
    }
runTestCase(testcase);


'''.replace('\n','\n').decode('utf-8')



e = EvalJs()
#e.execute(x)
