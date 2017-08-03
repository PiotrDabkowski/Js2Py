import pyjsparser
from space import Space
import fill_space
from byte_trans import ByteCodeGenerator
from code import Code
from simplex import MakeError
import sys
sys.setrecursionlimit(100000)


pyjsparser.parser.ENABLE_JS2PY_ERRORS = lambda msg: MakeError(u'SyntaxError', unicode(msg))

def eval_js_vm(js):
    a = ByteCodeGenerator(Code())
    s = Space()
    a.exe.space = s
    s.exe = a.exe

    d = pyjsparser.parse(js)

    a.emit(d)
    fill_space.fill_space(s, a)
    # print a.exe.tape
    a.exe.compile()

    return a.exe.run(a.exe.space.GlobalObj)


