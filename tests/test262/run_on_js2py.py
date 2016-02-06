import js2py
import os, re, traceback

init = r'''
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

function assert(mustBeTrue, message) {
    if (mustBeTrue === true) {
        return;
    }

    if (message === undefined) {
        message = 'Expected true but got ' + String(truthy);
    }
    $ERROR(message);
}

assert._isSameValue = function (a, b) {
    if (a === b) {
        // Handle +/-0 vs. -/+0
        return a !== 0 || 1 / a === 1 / b;
    }

    // Handle NaN vs. NaN
    return a !== a && b !== b;
};

assert.sameValue = function (actual, expected, message) {
    if (assert._isSameValue(actual, expected)) {
        return;
    }

    if (message === undefined) {
        message = 'Expected SameValue(' + String(actual) + ', ' + String(expected) + ') to be true';
    }
    $ERROR(message);
};

assert.notSameValue = function (actual, unexpected, message) {
    if (!assert._isSameValue(actual, unexpected)) {
        return;
    }

    if (message === undefined) {
        message = 'Expected SameValue(' + String(actual) + ', ' + String(unexpected) + ') to be false';
    }
    $ERROR(message);
};

assert.throws = function (expectedErrorConstructor, func) {
    if (func === undefined) {
        $ERROR('assert.throws requires two arguments: the error constructor and a function to run');
        return;
    }

    try {
        func();
    } catch (thrown) {
        if (typeof thrown !== 'object' || thrown === null) {
            $ERROR('Thrown value was not an object!');
            return;
        }
        if (thrown.constructor !== expectedErrorConstructor) {
            $ERROR('Expected a ' + expectedErrorConstructor.name + ' but got a ' + thrown.constructor.name);
        }
        return;
    }

    $ERROR('Expected a ' + expectedErrorConstructor.name + ' to be thrown but no exception was thrown at all');
};



'''

def load(path):
    with open(path, 'rb') as f:
        return f.read()


def exec_file(path):
    js = load(path)
    desc = re.search('/\*---(.+)---\*/', js, re.DOTALL).groups()[0]
    inc = re.search('includes:(.+)', desc, re.DOTALL)
    bibs = ''
    if inc:
        libs = inc.groups()[0].splitlines()
        har = 'harness/'
        for lib in libs:
            lib = lib.strip('[] -')
            if not lib:
                continue
            bibs += load(har+lib)
    try:
        js2py.eval_js(init + bibs + js)
    except NotImplementedError:
        return
    except:
        if 'negative:' in desc or 'onlyStrict' in desc:
            return # supposed to fail

        print '-'*30
        print traceback.format_exc()
        print
        print desc
        print
        print 'File "%s", line 1, in chuj' % os.path.abspath(path)
        raw_input()


def test_kind(kind, prototype=False, language=True):
    base_path = 'test/%s/' % ('built-ins' if not language else 'language') +kind
    if prototype=='all':
        for f in os.listdir(base_path):
            print f
            if os.path.isdir(os.path.join(base_path, f)):
                test_kind(kind, f)
        return
    if prototype:
        base_path = os.path.join(base_path, prototype)
    for f in sorted(os.listdir(base_path)):
        file = os.path.join(base_path, f)
        if os.path.isdir(file):
            continue
        print f
        exec_file(file)

test_kind('statements', 'try')
