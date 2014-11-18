"""This module translates JS flow into PY flow.

Translates:
IF ELSE

DO WHILE
WHILE
FOR 123
FOR iter
CONTINUE, BREAK, RETURN, LABEL, THROW, TRY, SWITCH
"""
from utils import *
from jsparser import *
from nodevisitor import exp_translator
import random

TO_REGISTER = []
CONTINUE_LABEL = 'JS_CONTINUE_LABEL_%s'
BREAK_LABEL = 'JS_BREAK_LABEL_%s'

def pass_white(source, start):
    n = start
    while n<len(source):
        if source[n] in {' ', '\n'}:
            n += 1
        else:
            break
    return n

def get_continue_label(label):
    return CONTINUE_LABEL%label.encode('hex')

def get_break_label(label):
    return BREAK_LABEL%label.encode('hex')

def pass_until(source, start, tokens=(';',)):
    while start < len(source) and source[start] not in tokens:
        start+=1
    return start+1


def except_keyword(source, start, keyword):
    """ Returns position after keyword if found else None
        Note: skips white space"""
    start = pass_white(source, start)
    kl = len(keyword)  #keyword len
    if kl+start >= len(source):
        return None
    if source[start:start+kl] != keyword:
        return None
    if source[start+kl] in IDENTIFIER_PART:
        return None
    return start + kl


def indent(lines, ind=4):
    return ind*' '+lines.replace('\n', '\n'+ind*' ').rstrip(' ')


def do_bracket_exp(source, start, throw=True):
    bra, cand = pass_bracket(source, start, '()')
    if throw and not bra:
        raise SyntaxError('Missing bracket expression')
    bra = exp_translator(bra[1:-1])
    if throw and not bra:
        raise SyntaxError('Empty bracket condition')
    return bra, cand if bra else start


def parse_identifier(source, start, throw=True):
    """passes white space from start and returns first identifier,
       if identifier invalid and throw raises SyntaxError otherwise returns None"""
    start = pass_white(source, start)
    end = start
    if source[end] not in IDENTIFIER_START:
        if throw:
            raise SyntaxError('Invalid identifier start: "%s"'%source[end])
        return None
    end += 1
    while end < len(source) and source[end] in IDENTIFIER_PART:
        end += 1
    if not is_valid_lval(source[start:end]):
        if throw:
            raise SyntaxError('Invalid identifier start: "%s"'%source[start:end])
        return None
    return source[start:end], end


def do_if(source, start):
    start += 2 # pass this if
    bra, start = do_bracket_exp(source, start, throw=True)
    statement, start = do_statement(source, start)
    if statement is None:
        raise SyntaxError('Invalid if statement')
    translated = 'if %s:\n'%bra+indent(statement)

    elseif = except_keyword(source, start, 'else')
    is_elseif = False
    if elseif:
        start = elseif
        if except_keyword(source, start, 'if'):
            is_elseif = True
        elseif, start = do_statement(source, start)
        if elseif is None:
            raise SyntaxError('Invalid if statement)')
        if is_elseif:
            translated += 'el' + elseif
        else:
            translated += 'else:\n'+ indent(elseif)
    return translated, start


def do_statement(source, start):
    """returns none if not found other functions that begin with 'do_' raise
    also this do_ type function passes white space"""
    start = pass_white(source, start)
    bra, cand = pass_bracket(source, start, '{}')
    if bra:
        return bra+'\n', cand
    else:
        return do_if(source, start)


def do_while(source, start):
    start += 5 # pass while
    bra, start = do_bracket_exp(source, start, throw=True)
    statement, start = do_statement(source, start)
    if statement is None:
        raise SyntaxError('Missing statement to execute in while loop!')
    return 'while %s:\n'%bra + indent(statement), start


def do_dowhile(source, start):
    start += 2 # pass do
    statement, start = do_statement(source, start)
    if statement is None:
        raise SyntaxError('Missing statement to execute in do while loop!')
    start = except_keyword(source, start, 'while')
    if not start:
        raise SyntaxError('Missing while keyword in do-while loop')
    bra, start = do_bracket_exp(source, start, throw=True)
    statement += 'if %s:\n' % bra + indent('break\n')
    return  'while 1:\n' + indent(statement), start


def do_block(source, start):
    bra, start = pass_bracket(source, start, '{}')
    print source[start:], bra
    return bra +'\n', start
    if bra is None:
        raise SyntaxError('Missing block ( {code} )')
    code = ''
    bra_pos = 1
    while True:
        st, bra_pos = do_statement(bra, bra_pos)
        if st is None:
            break
        code += st
    st = pass_white(bra, st)
    if source[st]!='}' or st+1!=len(bra): # has some more code that could not be parsed...
        raise SyntaxError('Could not parse source code, unknown statement')
    return code, source

def do_empty(source, start):
    return 'pass\n', start + 1

def do_expression(source, start):
    end = pass_until(source, start, tokens=(';',))
    if end==start+1: #empty statement
        return 'pass\n', end
    # Here I should add automatic semicolon insertion
    #todo auto ; insertion
    return exp_translator(source[start:end].rstrip(';'))+'\n', end

def do_var(source, start):
    #todo auto ; insertion
    start += 3 #pass var
    end = pass_until(source, start, tokens=(';',))
    defs = argsplit(source[start:end-1]) # defs is the list of defined vars with optional initializer
    code = ''
    for de in defs:
        var, var_end = parse_identifier(de, 0, True)
        TO_REGISTER.append(var)
        var_end = pass_white(de, var_end)
        if var_end<len(de): # we have something more to parse... It has to start with =
            if de[var_end] != '=':
                raise SyntaxError('Unexpected initializer in var statement. Expected "=", got "%s"'%de[var_end])
            code += exp_translator(de) + '\n'
    return code, end


def do_label(source, start):
    label, end = parse_identifier(source, start)
    end = pass_white(source, end)
    #now source[end] must be :
    assert source[end]==':'
    end += 1
    inside, end = do_statement(source, end)
    if inside is None:
        raise SyntaxError('Missing statement after label')
    defs = ''
    if inside.startswith('while ') or inside.startswith('for ') or inside.startswith('#for'):
        # we have to add contine label as well...
        # 3 or 1 since #for loop type has more lines before real for.
        sep = 1 if not inside.startswith('#for') else 3
        cont_label = get_continue_label(label)
        temp = inside.split('\n')
        injected = 'try:\n'+'\n'.join(temp[sep:])
        injected += 'except %s:\n    pass\n'%cont_label
        inside = '\n'.join(temp[:sep])+'\n'+indent(injected)
        defs += 'class %s(Exception): pass\n'%cont_label
    break_label = get_break_label(label)
    inside = 'try:\n%sexcept %s:\n    pass\n'% (indent(inside), break_label)
    defs += 'class %s(Exception): pass\n'%break_label
    return defs + inside, end


def do_for(source, start):
    start += 3 # pass for
    bra, start = pass_bracket(source, start , '()')
    inside, start = do_statement(source, start)
    if inside is None:
        raise SyntaxError('Missing statement after for')
    bra = bra[1:-1]
    if ';' in bra:
        init = argsplit(bra, ';')
        if len(init)!=3:
            raise SyntaxError('Invalid for statement')
        args = []
        for i, item in enumerate(init):
            end = pass_white(item, 0)
            if end==len(item):
                args.append('' if i!=1 else '1')
                continue
            if not i and except_keyword(item, end, 'var') is not None:
                # var statement
                args.append(do_var(item, end)[0])
                continue
            args.append(do_expression(item, end)[0])
        print args
        return '#for JS loop\n%swhile %s:\n%s%s\n' %(args[0], args[1].strip(), indent(inside), indent(args[2])), start
    # iteration
    end = pass_white(bra, 0)
    register = False
    if bra[end:].startswith('var '):
        end+=3
        end = pass_white(bra, end)
        register = True
    name, end = parse_identifier(bra, end)
    if register:
        TO_REGISTER.append(name)
    end = pass_white(bra, end)
    if bra[end:end+2]!='in' or bra[end+2] in IDENTIFIER_PART:
        raise SyntaxError('Invalid "for x in y" statement')
    end+=2 # pass in
    exp = exp_translator(bra[end:])
    res =  'for temp in %s:\n' % exp
    res += indent('var.put(%s, temp)\n' % name.__repr__()) + indent(inside)
    return res, start


# todo - IMPORTANT
def do_continue(source, start, name='continue'):
    start += len(name) #pass continue
    start = pass_white(source, start)
    if start<len(source) and source[start] == ';':
        return '%s\n'%name, start+1
    # labeled statement or error
    label, start = parse_identifier(source, start)
    start = pass_white(source, start)
    if start<len(source) and source[start] != ';':
        raise SyntaxError('Missing ; after label name in %s statement'%name)
    return 'raise %s("%s")\n' % (get_continue_label(label) if name=='continue' else get_break_label(label), name), start+1



def do_break(source, start):
    return do_continue(source, start, 'break')


def do_return(source, start):
    start += 6 # pass return
    end = pass_until(source, start)
    print end
    if end<len(source): #check whether we found ; or just run our of source code
        # found ;
        to = end-1
    else:
        # run out of source
        to = len(source)
    trans = exp_translator(source[start:to])
    return 'return %s\n' % (trans if trans else "var.get('undefined')"), end


# todo later?- Also important
def do_throw(source, start):
    start += 5 # pass return
    end = pass_until(source, start)
    print end
    if end<len(source): #check whether we found ; or just run our of source code
        # found ;
        to = end-1
    else:
        # run out of source
        to = len(source)
    trans = exp_translator(source[start:to])
    if not trans:
        raise SyntaxError('Invalid throw statement: nothing to throw')
    res = 'TempJsException = JsToPyException(%s)\nraise TempJsException\n' % trans
    return res, end


def do_try(source, start):
    start += 3 # pass try
    block, start = do_block(source, start)
    result = 'try:\n%s' %indent(block)
    catch = except_keyword(source, start, 'catch')
    if catch:
        bra, catch = pass_bracket(source, catch, '()')
        bra = bra[1:-1]
        print bra
        identifier, bra_end = parse_identifier(bra, 0)
        holder = 'PyJsHolder_%s_%d'%(identifier.encode('hex'), random.randrange(1e8))
        identifier = identifier.__repr__()
        bra_end = pass_white(bra, bra_end)
        if bra_end<len(bra):
            raise SyntaxError('Invalid content of catch statement')
        result += 'except PyJsException as PyJsTempException:\n'
        result += indent('%s = var.scope.get(%s)\n'%(holder, identifier))
        result += indent('var.scope[%s] = PyExceptionToJs(PyJsTempException)\n' % identifier)
        block, catch = do_block(source, catch)
        result += indent(block)
        result += indent('if %s is not None:\n' % holder)
        result += indent(indent('var.scope[%s] = %s\n' % (identifier, holder)))
        result += indent('else:\n')
        result += indent(indent('del var.scope[%s]\n' % identifier))
        result += indent('del %s\n' % holder)
    start = max(catch, start)
    final = except_keyword(source, start, 'finally')
    if not (final or catch):
        raise SyntaxError('Try statement has to be followed by catch or finally')
    if not final:
        return result, start
    # translate finally statement
    block, start = do_block(source, final)
    return result + 'finally:\n%s' % indent(block), start

# todo automatic ; insertion. fuck this crappy feature

# Least important
def do_switch(source, start):
    pass



#print do_dowhile('do {} while(k+f)', 0)[0]
#print 'e: "%s"'%do_expression('++(c?g:h);   mj', 0)[0]
print do_try('try {1} catch (j) {2} finally {3}', 0)[0]
print TO_REGISTER