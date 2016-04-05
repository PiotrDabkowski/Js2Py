from . import pyjsparser
#from pyesprima import esprima
from . import translating_nodes

import hashlib
import re

# the re below is how we'll recognise numeric constants.
# it finds any 'simple numeric that is not preceded with an alphanumeric character
# the numeric can be a float (so a dot is found) but
# it does not recognise notation such as 123e5, 0xFF, infinity or NaN
CP_NUMERIC_1 = re.compile(r'(?<![a-zA-Z0-9_"\'])([0-9\.]+)')
CP_NUMERIC_CONSTANT_PLACEHOLDER = '@@NUM_%i_NUM@@'
CP_NUMERIC_2 = re.compile(CP_NUMERIC_CONSTANT_PLACEHOLDER.replace('%i', r'([0-9\.]+)'))

# the re below is how we'll recognise string constants
# it finds a ' or ", then reads until the next matching ' or "
# this re only services simple cases, it can not be used when
# there are escaped quotes in the expression
CP_STRING_1 = re.compile(r'(["\'])(.*?)\1') # this is how we'll recognise string constants
CP_STRING_CONSTANT_PLACEHOLDER = "'@@STR_%i_STR@@'"
CP_STRING_2 = re.compile(CP_STRING_CONSTANT_PLACEHOLDER.replace('%i', r'(.*?)'))

cache = {}

# This crap is still needed but I removed it for speed reasons. Have to think of better idea
# import js2py.pyjs, sys
# # Redefine builtin objects... Do you have a better idea?
# for m in list(sys.modules):
# 	if m.startswith('js2py'):
# 		del sys.modules[m]
# del js2py.pyjs
# del js2py

DEFAULT_HEADER = u'''from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
'''


def dbg(x):
    """does nothing, legacy dummy function"""
    return ''

def translate_js(js, HEADER=DEFAULT_HEADER, use_compile_plan=False):
    """js has to be a javascript source code.
       returns equivalent python code."""
    if use_compile_plan:
        return translate_js_with_compile_plan(js, HEADER=HEADER)
    parser = pyjsparser.PyJsParser()
    parsed = parser.parse(js) # js to esprima syntax tree
    # Another way of doing that would be with my auto esprima translation but its much slower and causes import problems:
    # parsed = esprima.parse(js).to_dict()
    translating_nodes.clean_stacks()
    return HEADER + translating_nodes.trans(parsed)  # syntax tree to python code

def translate_js_with_compile_plan(js, HEADER=DEFAULT_HEADER):
    """js has to be a javascript source code.
       returns equivalent python code.

       compile plans only work with the following restrictions:
       - only enabled for oneliner expressions
       - when there are comments in the js code string substitution is disabled
       - when there nested escaped quotes string substitution is disabled, so

       cacheable:
       Q1 == 1 && name == 'harry'

       not cacheable:
       Q1 == 1 && name == 'harry' // some comment

       not cacheable:
       Q1 == 1 && name == 'o\'Reilly'

       not cacheable:
       Q1 == 1 && name /* some comment */ == 'o\'Reilly'
       """
    if not r'\"' in js and not r"\'" in js and not r'//' in js and not '/*' in js:
        # since our regex for strings can't understand newlines don't optimize
        hasliterals = "'" in js or '"' in js
    else:
        hasliterals = False

    class match_increaser(object):
        matchcount = 0

        def __init__(self, mask):
            self.mask = mask
            self.matches = []

        def __call__(self, match):
            self.matchcount += 1
            self.matches.append(match.group(0))
            return self.mask%self.matchcount

    match_increaser_num = match_increaser(CP_NUMERIC_CONSTANT_PLACEHOLDER)
    compile_plan = re.sub(CP_NUMERIC_1, match_increaser_num, js)
    if hasliterals:
        match_increaser_str = match_increaser(CP_STRING_CONSTANT_PLACEHOLDER)
        compile_plan = re.sub(
            CP_STRING_1, match_increaser_str, compile_plan
        )
    compile_plan = re.sub(CP_NUMERIC_2, "'" + CP_NUMERIC_CONSTANT_PLACEHOLDER.replace('%i', r'\1') + "'", compile_plan)

    cp_hash = hashlib.md5(compile_plan).digest()
    try:
        python_code = cache[cp_hash]['proto_python_code']
    except:
        parser = pyjsparser.PyJsParser()
        parsed = parser.parse(compile_plan) # js to esprima syntax tree
        # Another way of doing that would be with my auto esprima translation but its much slower and causes import problems:
        # parsed = esprima.parse(js).to_dict()
        translating_nodes.clean_stacks()
        python_code = translating_nodes.trans(parsed)  # syntax tree to python code
        cache[cp_hash] = {
            'compile_plan': compile_plan,
            'proto_python_code': python_code,
        }
    for counter, value in enumerate(match_increaser_num.matches):
        python_code = python_code.replace("u'" + CP_NUMERIC_CONSTANT_PLACEHOLDER%(counter+1) + "'", value, 1)

    if hasliterals:
        for counter, value in enumerate(match_increaser_str.matches):
            python_code = python_code.replace(CP_STRING_CONSTANT_PLACEHOLDER%(counter+1), value, 1)

    return HEADER + python_code

def trasnlate(js, HEADER=DEFAULT_HEADER):
    """js has to be a javascript source code.
       returns equivalent python code.

       Equivalent to translate_js"""
    return translate_js(js, HEADER)

syntax_tree_translate = translating_nodes.trans

if __name__=='__main__':
    PROFILE = False
    import js2py
    import codecs
    def main():
        with codecs.open("esprima.js", "r", "utf-8") as f:
            d = f.read()
            r = js2py.translate_js(d)

            with open('res.py','wb') as f2:
                f2.write(r)
            exec(r, {})
    if PROFILE:
        import cProfile
        cProfile.run('main()', sort='tottime')
    else:
        main()