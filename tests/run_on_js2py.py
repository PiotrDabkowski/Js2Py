import js2py
from js2py.base import PyJsException, PyExceptionToJs
import os, sys, re, traceback
from distutils.version import LooseVersion


def load(path):
    with open(path, 'r') as f:
        return f.read()



INCLUDE_PATH = 'includes/'
TEST_PATH = 'test_cases/'
INIT = load(os.path.join(INCLUDE_PATH, 'init.js'))


class TestCase:
    description = None
    includes = None
    author = None
    es5id = None
    negative = None
    info = None
    flags = []
    CATEGORY_REQUIRES_SPLIT = {'flags', 'includes'}

    def __init__(self, path):

        self.path = path
        self.full_path = os.path.abspath(self.path)
        self.clear_name = '/'.join(self.full_path.split(os.sep)[-3-('prototype' in self.full_path):-1])
        self.raw = load(self.path)

        self._parse_test_info()

        self.init = INIT

        if self.includes:
            for include in self.includes:
                self.init += load(os.path.join(INCLUDE_PATH, include))
        if 'onlyStrict' in self.flags:
            self.strict_only = True
        else:
            self.strict_only = False

        self.code = self.init + self.raw

    def _parse_test_info(self):
        self.raw_info = re.search('/\*---(.+)---\*/', self.raw, re.DOTALL).groups()[0].strip()
        category = None
        category_content = None
        for line in self.raw_info.splitlines() + ['END:']:
            if line.startswith(' '):
                if category is None:
                    raise RuntimeError('Could not parse test case info! %s' % self.path)
                category_content += '\n' + line.lstrip()
            else:
                if category is not None:
                    content = category_content.strip()
                    content = content if not category in self.CATEGORY_REQUIRES_SPLIT else self._content_split(content)
                    setattr(self, category, content)
                start_index = line.index(':')
                category = line[:start_index]
                category_content = line[start_index+1:].lstrip(' >\n')

    def _content_split(self, content):
        res = []
        for c in content.splitlines():
            cand = c.strip('[] -')
            if cand:
                res.append(cand)
        return res

    def run(self):
        # labels: 'PASSED', 'FAILED', 'CRASHED', 'NOT_IMPLEMENTED', 'NO_FAIL'
        errors = True
        crashed = True
        label = None
        try:
            js2py.eval_js(self.code)
            errors = False
            crashed = False

        except NotImplementedError:
            tb = sys.exc_info()[-1]
            stk = traceback.extract_tb(tb)
            fname = stk[-1][2]
            passed = False
            reason = 'Not implemented - "%s"' % fname
            full_error = traceback.format_exc()
            label = 'NOT_IMPLEMENTED'

        except PyJsException, e:
            crashed = False
            full_error = traceback.format_exc()
            if self.negative:
                passed = True
            else:
                passed = False
                reason = PyExceptionToJs(e).get('message').to_python()
                label = 'FAILED'


        except SyntaxError, e:
            full_error = traceback.format_exc()
            if self.negative=='SyntaxError':
                passed = True
            else:
                passed = False
                reason = 'Could not parse'
                label = 'CRASHED'

        except:
            full_error = traceback.format_exc()
            passed = False
            reason = 'UNKNOWN - URGENT, FIX NOW!'
            label = 'CRASHED'

        if not errors:
            if self.negative:
                passed = False
                reason = "???"
                label = "NO_FAIL"
                full_error = ''
            else:
                passed = True

        if passed:
            label = "PASSED"
            reason = ''
            full_error = ''
        self.passed, self.label, self.reason, self.full_error = passed, label, reason, full_error
        return passed, label, reason, full_error

    def print_result(self):

        print self.clear_name, self.es5id, self.label, self.reason




def list_path(path, folders=False):
    res = []
    for f in os.listdir(path):
        full = os.path.join(path, f)
        is_file = os.path.isfile(full)
        if (folders and not is_file) or (not folders and is_file):
            res.append(full)
    if folders:
        return sorted(res)
    else:
        return sorted(res, key=LooseVersion)

def test_all(path):
    files = list_path(path)
    folders = list_path(path, folders=True)
    for f in files:
        if not f.endswith('.js'):
            continue
        test = TestCase(f)
        if test.strict_only:
            continue
        test.run()
        test.print_result()
    for folder in folders:
        test_all(folder)



test_all(TEST_PATH)


