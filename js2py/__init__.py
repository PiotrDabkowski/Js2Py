""" This module allows you to translate and execute Javascript in pure python.
    Basically its implementation of ECMAScript 5.1 in pure python.

    Use eval_js method to execute javascript code and get resulting python object.

    Or use EvalJs to execute many javascript code fragments under same context - you would be able to get any
    variable from the context! Also you can use its console method to play with interactive javascript console.

    NOTE: This module is still not fully finished:
          Date and JSON builtin objects are not implemented
          Array prototype is not fully finished
          Bitwise operations are not implemented
          Other than that everything should work fine.

          Finishing all these would take me about 30 hours and I can't afford this time now.
          Fortunately for typical javascript code with semicolons inserted the translator should work fine :)
"""
__author__ = 'Piotr Dabkowski'
__all__  = ['EvalJs', 'translate_js', 'import_js', 'eval_js', 'parse_js']
from js2py.evaljs import *
from translators import parse as parse_js

