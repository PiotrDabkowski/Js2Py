__all__ = ['PyJsParser', 'Node', 'WrappingNode', 'node_to_dict', 'parse', 'translate_js', 'translate', 'syntax_tree_translate',
           'DEFAULT_HEADER']
__author__ = 'Piotr Dabkowski'
__version__ = '2.2.0'
from pyjsparser import PyJsParser, Node, WrappingNode, node_to_dict
from translator import translate_js, trasnlate, syntax_tree_translate, DEFAULT_HEADER


def parse(javascript_code):
    """Returns syntax tree of javascript_code.

    Syntax tree has the same structure as syntax tree produced by esprima.js

       Same as PyJsParser().parse  For your convenience :) """
    p = PyJsParser()
    return p.parse(javascript_code)


