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

def pass_white(source, start):
    n = start
    while n<len(source):
        if source[n] in {' ', '\n'}:
            n += 1
        else:
            break
    return n

def except_keyword(source, start, keyword):
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
    bra, cand = pass_bracket(source, start)  #parse () after if
    if throw and not bra:
        raise SyntaxError('Missing bracket expression')
    bra = exp_translator(bra[1:-1])
    if throw and not bra:
        raise SyntaxError('Empty bracket condition')
    return bra, cand if bra else start

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

print do_dowhile('do{}while(k+f)', 0)[0]
