import pyjsparser
import translating_nodes

DEFAULT_HEADER = u'''from js2py.pyjs import *\nvar = Scope( JS_BUILTINS )\nset_global_object(var)\n'''

def dbg(x):
    """does nothing, legacy dummy function"""
    return ''

def translate_js(js, HEADER=DEFAULT_HEADER):
    """js has to be a javascript source code.
       returns equivalent python code."""
    parser = pyjsparser.PyJsParser()
    parsed = parser.parse(js) # js to esprima syntax tree
    return HEADER + translating_nodes.trans(parsed)  # syntax tree to python code

def trasnlate(js, HEADER=DEFAULT_HEADER):
    """js has to be a javascript source code.
       returns equivalent python code.

       Equivalent to translate_js"""
    return translate_js(js, HEADER)

syntax_tree_translate = translating_nodes.trans

if __name__=='__main__':
    import js2py
    import codecs
    with codecs.open("esp.js", "r", "utf-8") as f:
        d = f.read()
        r = translate_js(d)
        r = translate_js(d)
        with open('res.py','w') as f2:
            f2.write(r)
    print js2py.eval_js(d)