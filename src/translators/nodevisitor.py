from jsparser import *
from utils import *
import re, time
from utils import *
REPL = {}

def split_at_any(text, lis, translate=False):
    """lis must be sorted from longest ele to shortest"""
    last = 0
    n = 0
    text_len = len(text)
    while n<text_len:
        for e in lis:
            s = len(e)
            if s+n>text_len:
                continue
            if e==text[n:n+s]:
                yield text[last:n] if not translate else NodeVisitor(text[last:n]).translate()
                yield e
                n+=s
                last = n
                break
        else:
            n+=1
    yield text[last:n] if not translate else NodeVisitor(text[last:n]).translate()



class NodeVisitor:
    def __init__(self, code):
        self.code = code

    def rl(self, lis, op):
        """performs this operation on a list from *right to left*
        op must take 2 args"""
        it = reversed(lis)
        res = NodeVisitor(it.next()).translate()
        for e in it:
            e = NodeVisitor(e).translate()
            res = op(e, res)
        return res

    def lr(self, lis, op):
        """performs this operation on a list from *left to right*
        op must take 2 args"""
        it = iter(lis)
        res = NodeVisitor(it.next()).translate()
        for e in it:
            e = NodeVisitor(e).translate()
            res = op(e, res)
        return res

    def translate(self):
        new = ''
        for e in bracket_split(self.code, ['()','[]'], False):
            if e[0]=='[':
                name = '#PYJSREPL'+str(len(REPL))+'#'
                new+= name
                REPL[name] = e
            elif e[0]=='(': # can be a function call
                name = '@PYJSREPL'+str(len(REPL))+'@'
                new+= name
                REPL[name] = e
        #Check comma operator:
        cand = new.split(',')
        if len(cand)>1:
            return self.rl(cand, self.comma)
        #Check = operator:
        cand = new.split('=')
        if len(cand)>1:
            it = reversed(cand)
            res =  NodeVisitor(it.next().strip()).translate()
            for e in it:
                op = ''
                if e[-1] in OP_METHODS:
                    op = ','+e[-1]
                    e = e[:-1]
                elif e[-2:] in OP_METHODS:
                    op =  ','+e[-2:]
                    e = e[:-2]
                e = NodeVisitor(e.strip()).translate()
                #Now replace last get method with put and change args
                c = list(bracket_split(e, ['()']))
                beg, arglist = ''.join(c[:-1]).strip(), c[-1].strip()  #strips just to make sure... I will remove it later
                if beg[-4:0]!='.get':
                    raise SyntaxError('Invalid left-hand side in assignment')
                beg = beg[0:-3]+'put'
                arglist = arglist[0:-1]+', '+res+op+')'
                res = beg+arglist
        # Find this crappy ?:
        if '?' in new:
            res  = split_at_any(new, [':', '?'], translate=True)
            return transform_crap(res)
        #Now check remaining 2 arg operators



    def comma(self, a, b):
        return 'PyJsComma('+a+','+b+')'



def transform_crap(code):
    """Transforms this ?: crap into if else python syntax"""
    ind = code.rfind('?')
    if ind==-1:
        return code
    sep = code.find(':', ind)
    if sep==-1:
        raise SyntaxError('Invalid ?: syntax (probably missing ":" )')
    beg = min(code.rfind(':', ind), code.find('?', ind))+1
    end = code.find('?',sep)
    end = len(code) if end==-1 else end
    formula = '('+code[ind+1:sep]+' if '+code[beg:ind]+' else '+code[sep+1:end]+')'
    return transform_crap(code[:beg if not beg else beg-1]+formula+code[end:])
