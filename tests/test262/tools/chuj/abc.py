
import logging
import optparse
import os
from os import path
import platform
import re
import subprocess
import sys
import tempfile
import time
import xml.dom.minidom
import datetime
import shutil
import json
import stat
import xml.etree.ElementTree as xmlj
import unicodedata
from collections import Counter

from parseTestRecord import parseTestRecord, stripHeader

from packagerConfig import *



class Case(object):
    def __init__(self, full_path):
        self.name = os.path.basename(full_path)
        self.suite = self
        self.full_path = full_path
        self.strict_mode = False
        f = open(self.full_path)
        self.contents = f.read()
        f.close()
        testRecord = parseTestRecord(self.contents, self.name)
        self.test = testRecord["test"]
        del testRecord["test"]
        del testRecord["header"]
        testRecord.pop("commentary", None)  # do not throw if missing
        self.testRecord = testRecord

    def NegativeMatch(self, stderr):
        neg = re.compile(self.GetNegative())
        return re.search(neg, stderr)

    def GetNegative(self):
        return self.testRecord['negative']

    def GetName(self):
        return path.join(*self.name)

    def GetMode(self):
        if self.strict_mode:
            return "strict mode"
        else:
            return "non-strict mode"

    def GetPath(self):
        return self.name

    def IsNegative(self):
        return 'negative' in self.testRecord

    def IsOnlyStrict(self):
        return 'onlyStrict' in self.testRecord

    def IsNoStrict(self):
        return 'noStrict' in self.testRecord

    def IsAsyncTest(self):
        return '$DONE' in self.test

    def GetInclude(self, name):
        return get_include(name)

    def GetIncludeList(self):
        if self.testRecord.get('includes'):
            return self.testRecord['includes']
        return re.findall('\$INCLUDE\([\'"]([^\)]+)[\'"]\)', self.test)

    def GetAdditionalIncludes(self):
        return '\n'.join([self.suite.GetInclude(include) for include in self.GetIncludeList()])

    def WrapTest(self):
        return """
try {
""" + self.test + """\n;RES123 = 'PASSED7486'
} catch(e) {
    RES123 = e.message
}
RES123
"""

    def GetSource(self):
        # "var testDescrip = " + str(self.testRecord) + ';\n\n' + \
        source = self.suite.GetInclude("sta.js") + \
                 self.suite.GetInclude("cth.js") + \
                 self.suite.GetInclude("assert.js")

        if self.IsAsyncTest():
            source = source + \
                     self.suite.GetInclude("timer.js") + \
                     self.suite.GetInclude("doneprintHandle.js").replace('print', self.suite.print_handle)

        source = source + \
                 self.GetAdditionalIncludes() + \
                 self.WrapTest() + '\n'

        if self.strict_mode:
            source = '"use strict";\nvar strict_mode = true;\n' + source
        else:
            # add comment line so line numbers match in both strict and non-strict version
            source = '//"no strict";\nvar strict_mode = false;\n' + source

        return source

    def InstantiateTemplate(self, template, params):
        def GetParameter(match):
            key = match.group(1)
            return params.get(key, match.group(0))

        return placeHolderPattern.sub(GetParameter, template)






def get_include(name):
    path = '/Users/PiotrDabkowski/PycharmProjects/Js2Py/tests/test262/harness/' + name
    f = open(path)
    contents = stripHeader(f.read())
    contents = re.sub(r'\r\n', '\n', contents)
    res = contents + "\n"
    f.close()
    return res

import js2py
TEST_PATH = '/Users/PiotrDabkowski/PycharmProjects/Js2Py/tests/test262/test/'


test_object = 'Object'
test_folder = 'built-ins'

a = Case('/Users/PiotrDabkowski/PycharmProjects/Js2Py/tests/test262/test/built-ins/String/15.5.5.5.2-3-1.js').GetSource()
PASSED = 0
FAILED = 0
CRUSHED = 0
def do_folder(folder):
    global PASSED, FAILED, CRUSHED
    print 'Doing', folder
    folders = []
    f = os.path.join(TEST_PATH, folder)

    for e in os.listdir(f):
        e = os.path.join(f, e)
        if os.path.isfile(e):
            case = Case(e)
            if case.IsOnlyStrict():
                print 'Strict', case.name
                continue
            code = case.GetSource()
            try:
                res = js2py.eval_js(code)
                if res == 'PASSED7486':
                    PASSED += 1
                    continue
                else:
                    FAILED += 1
                    print
                    print 'Failed', case.name
                    print res
                    print
            except KeyboardInterrupt:
                return
            except:
                CRUSHED += 1
                print '<<<<<<<<<<<<<<'
                print 'Crushed', case.name
                print '<<<<<<<<<<<<<<<'
        else:
            folders.append(e)
    print 'Passed ', PASSED, 'out of', PASSED + FAILED + CRUSHED, 'tests. ', CRUSHED, 'crushed.'
    for f in folders:
        do_folder(f)




folder = os.path.join( test_folder, test_object)
do_folder(folder)



raw_input()












