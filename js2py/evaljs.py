# coding=utf-8
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
        #print code
        exec code in self.context

    def eval(self, expression):
        """evaluates expression in current context and returns its value"""
        code = 'PyJsEvalResult = eval(%s)'%repr(expression)
        self.execute(code)
        return self['PyJsEvalResult']


    def __getattr__(self, var):
        return self.get_variable(var)

    def get_variable(self, var):
        """returns variable from global JS context"""
        return self.context['var'].get(var)

    def __getitem__(self, var):
        return self.get_variable(var)

    def console(self):
        """starts to interact (starts interactive console) Something like code.InteractiveConsole"""
        while True:
            code = raw_input('>>> ')
            try:
                print self.eval(code)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print 'EXCEPTION: '+str(e)



x = ur'''
var p = 50;
console.log(eval('if (1) 5;'));

'''.replace('\n','\n').decode('utf-8')

#with open('C:\Users\Piotrek\Desktop\esprima.js', 'rb') as f:
#    x2 = f.read()


if __name__=='__main__':
    e = EvalJs()
    #e.interact()

