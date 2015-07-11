# coding=utf-8
""" This module is still experimental!
"""
from translators.translator import translate_js, dbg
import sys
import time
import json
__all__  = ['EvalJs', 'translate_js', 'import_js', 'eval_js']

def import_js(path, globals):
    """Imports from javascript source file. Note may cause name conflicts.
      globals is your globals()"""
    with open(path, 'rb') as f:
        js = f.read()
    e = EvalJs()
    e.execute(js)
    var = e.context['var']
    for name in var:
        globals[name] = var.get(name)

def eval_js(js):
    """Just like javascript eval. Translates javascript to python,
       executes and returns python object.
       js is javascript source code"""
    e = EvalJs()
    return e.eval(js)



class EvalJs(object):
    """This class supports continuous execution of javascript under same context.

       You can run interactive javascript console with console method!"""
    def __init__(self, context=None):
        self.context = {}
        self.__started = False

    def execute(self, js):
        """executes javascript js in current context"""
        try:
            if not self.__started:
                code = translate_js(js)
                self.__started = True
            else:
                code = translate_js(js, '')
        except:
            dbg(js)
            raise
        dbg(code)
        #print code
        exec code in self.context

    def eval(self, expression):
        """evaluates expression in current context and returns its value"""
        code = 'PyJsEvalResult = eval(%s)'%json.dumps(expression)
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
                import traceback
                if DEBUG:
                    sys.stderr.write(traceback.format_exc())
                else:
                    sys.stderr.write('EXCEPTION: '+str(e)+'\n')
                time.sleep(0.01)



x = r'''
var return;
'''.replace('\n','\n').decode('unicode-escape')

#print x

DEBUG = True

if __name__=='__main__':
    #with open('C:\Users\Piotrek\Desktop\esprima.js', 'rb') as f:
    #    x = f.read()
    e = EvalJs()
    #e.execute(x)
    e.console()

