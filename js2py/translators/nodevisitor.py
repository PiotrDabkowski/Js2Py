from jsparser import *
from utils import *
import re
from utils import *

#Note all white space sent to this module must be ' ' so no '\n'
REPL = {}


#PROBLEMS
# <<=, >>=, >>>=
# they are unusual so I will not fix that now. a++ +b works fine and a+++++b  (a++ + ++b) does not work even in V8

def bracket_replace(code):
    new = ''
    for e in bracket_split(code, ['()','[]'], False):
        if e[0]=='[':
            name = '#PYJSREPL'+str(len(REPL))+'{'
            new+= name
            REPL[name] = e
        elif e[0]=='(': # can be a function call
            name = '@PYJSREPL'+str(len(REPL))+'}'
            new+= name
            REPL[name] = e
        else:
            new+=e
    return new

class NodeVisitor:
    def __init__(self, code):
        self.code = code

    def rl(self, lis, op):
        """performs this operation on a list from *right to left*
        op must take 2 args
        a,b,c  => op(a, op(b, c))"""
        it = reversed(lis)
        res = trans(it.next())
        for e in it:
            e = trans(e)
            res = op(e, res)
        return res

    def lr(self, lis, op):
        """performs this operation on a list from *left to right*
        op must take 2 args
        a,b,c  => op(op(a, b), c)"""
        it = iter(lis)
        res = trans(it.next())
        for e in it:
            e = trans(e)
            res = op(res, e)
        return res

    def translate(self):
        """Translates outer operation and calls translate on inner operation.
           Returns fully translated code."""
        if not self.code:
            return ''
        new = bracket_replace(self.code)
        #Check comma operator:
        cand = new.split(',') #every comma in new must be an operator
        if len(cand)>1:  #LR
            return self.lr(cand, js_comma)
        #Check = operator:
        # dont split at != or !== or == or === or <= or >=
        #note <<=, >>= or this >>> will NOT be supported
        # maybe I will change my mind later
        cand = list(split_at_single(new, '=', ['!', '=','<','>'], ['=']))
        if len(cand)>1: # RL
            it = reversed(cand)
            res =  trans(it.next())
            for e in it:
                e = e.strip()
                if not e:
                    raise SyntaxError('Missing left-hand in assignment!')
                op = ''
                if e[-2:] in OP_METHODS:
                    op =  ','+e[-2:].__repr__()
                    e = e[:-2]
                elif e[-1:] in OP_METHODS:
                    op = ','+e[-1].__repr__()
                    e = e[:-1]
                e = trans(e)
                #Now replace last get method with put and change args
                c = list(bracket_split(e, ['()']))
                beg, arglist = ''.join(c[:-1]).strip(), c[-1].strip()  #strips just to make sure... I will remove it later
                if beg[-4:]!='.get':
                    raise SyntaxError('Invalid left-hand side in assignment')
                beg = beg[0:-3]+'put'
                arglist = arglist[0:-1]+', '+res+op+')'
                res = beg+arglist
            return res
        # Find this crappy ?:
        if '?' in new:
            res  = ''.join(split_at_any(new, [':', '?'], translate=trans))
            return transform_crap(res)
        #Now check remaining 2 arg operators that are not handled by python
        #They all have Left to Right (LR) associativity
        order = [OR, AND, BOR, BXOR, BAND, EQS, COMPS, BSHIFTS, ADDS, MULTS]
        # actually we dont need OR and AND because they can be handled easier. But just for fun
        dangerous = ['<', '>']
        for typ in order:
            #we have to use special method for ADDS since they can be also unary operation +/++ or -/-- FUCK
            if '+' in typ:
                cand = list(split_add_ops(new))
            else:
               cand = list(split_at_any(new, typ.keys(), False, dangerous, dangerous))  #dont translate and cant start on end on dangerous op.
            if not len(cand)>1:
                continue
            n = 1
            res = trans(cand[0])
            if not res:
                raise SyntaxError("Missing operand!")
            while n<len(cand):
                e = cand[n]
                if not e:
                    raise SyntaxError("Missing operand!")
                if n%2:
                    op = typ[e]
                else:
                    res = op(res, trans(e))
                n+=1
            return res
        #Now replace unary operators - only they are left
        cand = list(split_at_any(new, UNARY.keys(), False))
        if len(cand)>1: #contains unary operators
            if '++' in cand or '--' in cand: #it cant contain both ++ and --
                if '--' in cand:
                    op = '--'
                    meths = js_post_dec, js_pre_dec
                else:
                    op = '++'
                    meths = js_post_inc, js_pre_inc
                pos = cand.index(op)
                if cand[pos-1].strip(): # post increment
                    a = cand[pos-1]
                    meth = meths[0]
                elif cand[pos+1].strip(): #pre increment
                    a = cand[pos+1]
                    meth = meths[1]
                else:
                    raise SyntaxError('Invalid use of ++ operator')
                if cand[pos+2:]:
                    raise SyntaxError('Too many operands')
                operand = meth(trans(a))
                cand = cand[:pos-1]
            # now last cand should be operand and every other odd element should be empty
            else:
                operand = trans(cand[-1])
                del cand[-1]
            for i, e in enumerate(reversed(cand)):
                if i%2:
                    if e.strip():
                        raise SyntaxError('Too many operands')
                else:
                    operand = UNARY[e](operand)
            return operand
        #Replace brackets
        if new[0]=='@' or new[0]=='#':
            if len(list(bracket_split(new, ('#{','@}')))) ==1: # we have only one bracket, otherwise pseudobracket like @@....
                assert new in REPL
                if new[0]=='#':
                    raise SyntaxError('[] cant be used as brackets! Use () instead.')
                return '('+trans(REPL[new][1:-1])+')'
        #Replace function calls and prop getters
        # 'now' must be a reference like: a or b.c.d but it can have also calls or getters ( for example a["b"](3))
        #From here @@ means a function call and ## means get operation (note they dont have to present)
        it = bracket_split(new, ('#{','@}'))
        res = []
        for e in it:
            if e[0]!='#' and e[0]!='@':
                res += [x.strip() for x in e.split('.')]
            else:
                res += [e.strip()]
        # res[0] can be inside @@ (name)...
        res = filter(lambda x: x, res)
        if is_internal(res[0]):
            out = res[0]
        elif res[0][0] in {'#', '@'}:
            out = '('+trans(REPL[res[0]][1:-1])+')'
        elif is_lval(res[0]):
            out = 'var.get('+res[0].__repr__()+')'
        else:
            raise SyntaxError('Invalid identifier: "%s"'%res[0])
        if len(res)==1:
            return out
        n = 1
        while n<len(res): #now every func call is a prop call
            e = res[n]
            if e[0]=='@': # direct call
                out += trans_args(REPL[e])
                n += 1
                continue
            args = False #assume not prop call
            if n+1<len(res) and res[n+1][0]=='@': #prop call
                args = trans_args(REPL[res[n+1]])[1:]
                if args!=')':
                    args = ','+args
            if e[0]=='#':
                prop = trans(REPL[e][1:-1])
            else:
                if not is_lval(e):
                    raise SyntaxError('Invalid identifier: "%s"'%e)
                prop = e.__repr__()
            if args: # prop call
                n+=1
                out += '.callprop('+prop+args
            else: #prop get
                out += '.get('+prop+')'
            n+=1
        return out

def js_comma(a, b):
    return 'PyJsComma('+a+','+b+')'

def js_or(a, b):
    return '('+a+' or '+b+')'

def js_bor(a, b):
    return '('+a+'|'+b+')'

def js_bxor(a, b):
    return '('+a+'^'+b+')'

def js_band(a, b):
    return '('+a+'&'+b+')'

def js_and(a, b):
    return '('+a+' and '+b+')'
def js_strict_eq(a, b):

    return 'PyJsStrictEq('+a+','+b+')'

def js_strict_neq(a, b):
    return 'PyJsStrictNeq('+a+','+b+')'

#Not handled by python in the same way like JS. For example 2==2==True returns false.
# In JS above would return true so we need brackets.
def js_abstract_eq(a, b):
    return '('+a+'=='+b+')'

#just like ==
def js_abstract_neq(a, b):
    return '('+a+'!='+b+')'

def js_lt(a, b):
    return '('+a+'<'+b+')'

def js_le(a, b):
    return '('+a+'<='+b+')'

def js_ge(a, b):
    return '('+a+'>='+b+')'

def js_gt(a, b):
    return '('+a+'>'+b+')'

def js_in(a, b):
    return a+'.contains('+b+')'

def js_instanceof(a, b):
    return a+'.instanceof('+b+')'

def js_lshift(a, b):
    return '('+a+'<<'+b+')'

def js_rshift(a, b):
    return '('+a+'>>'+b+')'

def js_shit(a, b):
    return 'PyJsBshift('+a+','+b+')'

def js_add(a, b):  # To simplify later process of converting unary operators + and ++
    return '(%s+%s)'%(a, b)

def js_sub(a, b):  # To simplify
    return '(%s-%s)'%(a, b)

def js_mul(a, b):
    return '('+a+'*'+b+')'

def js_div(a, b):
    return '('+a+'/'+b+')'

def js_mod(a, b):
    return '('+a+'%'+b+')'

def js_typeof(a):
    return a+'.typeof()'

def js_void(a):
    return '('+a+')'

def js_new(a):
    # i am not sure here yet
    #case 1: got object without calling, in this case a will end with .get(...)
    #        we should simply add .create() at the end
    #case2: got object with calling without callprop.
    return a+'.create()'

def js_delete(a):
    # To simplify
    #replace last get with delete.
    return a

def js_neg(a):
    return '(-'+a+')'

def js_pos(a):
    return '(+'+a+')'

def js_inv(a):
    return '(~'+a+')'

def js_not(a):
    return a+'.neg()'

def js_pre_inc(a):
    return a+'.PreInc()'

def js_post_inc(a):
    return a+'.PostInc()'

def js_pre_dec(a):
    return a+'.PreDec()'

def js_post_dec(a):
    return a+'.PostDec()'


OR = {'||': js_or}
AND = {'&&': js_and}
BOR = {'|': js_bor}
BXOR = {'^': js_bxor}
BAND = {'&': js_band}

EQS = {'===': js_strict_eq,
       '!==': js_strict_neq,
       '==': js_abstract_eq, # we need == and != too. Read a note above method
       '!=': js_abstract_neq}

#Since JS does not have chained comparisons we need to implement all cmp methods.
COMPS = {'<': js_lt,
         '<=': js_le,
         '>=': js_ge,
         '>': js_gt,
         ' instanceof ': js_instanceof,
         ' in ': js_in}

BSHIFTS = {'<<': js_lshift,
           '>>': js_rshift,
           '>>>': js_shit}

ADDS = {'+': js_add,
        '-': js_sub}

MULTS = {'*': js_mul,
         '/': js_div,
         '%': js_mod}


#Note they dont contain ++ and -- methods because they both have 2 different methods
# correct method will be found automatically in translate function
UNARY = {'typeof ': js_typeof,
         'void ': js_void,
         'new ': js_new,
         'delete ': js_delete,
         '!': js_not,
         '-': js_neg,
         '+': js_pos,
         '~': js_inv,
         '++': None,
         '--': None
         }


def transform_crap(code): #needs some more tests
    """Transforms this ?: crap into if else python syntax"""
    ind = code.rfind('?')
    if ind==-1:
        return code
    sep = code.find(':', ind)
    if sep==-1:
        raise SyntaxError('Invalid ?: syntax (probably missing ":" )')
    beg = max(code.rfind(':', 0, ind), code.find('?', 0, ind))+1
    end = code.find(':',sep+1)
    end = len(code) if end==-1 else end
    formula = '('+code[ind+1:sep]+' if '+code[beg:ind]+' else '+code[sep+1:end]+')'
    return code[:beg]+formula+code[end:]


from code import InteractiveConsole

#e = InteractiveConsole(globals()).interact()

def trans(code):
    return NodeVisitor(code.strip()).translate().strip()

#todo finish this trans args
def trans_args(code):
    new = bracket_replace(code.strip()[1:-1])
    args = ','.join(trans(e) for e in new.split(','))
    return '(%s)'%args


def exp_translator(code):
    global REPL
    REPL = {}
    assert '\n' not in code
    assert '@' not in code
    assert ';' not in code
    assert '#' not in code
    #if not code.strip(): #?
    #    return 'var.get("undefined")'
    return trans(code)

if __name__=='__main__':
    #print 'Here',  trans('(eee   )  .   ii  [  PyJsMarker   ]  [   jkj  ]  (  j  ,   j  )  .   jiji   (h  ,  ji  ,  i)(non  )(  )()()()')
    for e in xrange(3):
        print  exp_translator('jk = kk.ik++')
    #First line translated with PyJs:  PyJsStrictEq(PyJsAdd((Js(100)*Js(50)),Js(30)), Js("5030")), yay!

