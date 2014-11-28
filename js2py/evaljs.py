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
        exec code in self.context

    def __getattr__(self, var):
        return self.get_variable(var)

    def get_variable(self, var):
        """returns variable from global JS context"""
        return self.context['var'].get(var)

    def __getitem__(self, var):
        return self.get_variable(var)


x = r'''
console.log(Object('abcdef') + '9');
'''



e = EvalJs()
e.execute(x)
