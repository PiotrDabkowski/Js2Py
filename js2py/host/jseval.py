from js2py.base import *
from translators.translator import translate_js
import inspect


@Js
def Eval(code):
    local_scope = inspect.stack()[3][0].f_locals['var']
    global_scope = this.GlobalObject
    # todo fix scope - we have to behave differently if called through variable other than eval
    # we will use local scope (default)
    globals()['var'] = local_scope
    py_code = translate_js(code.to_string().value, '')
    executor(py_code)


def executor(code):
    exec code in globals()

