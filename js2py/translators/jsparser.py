"""
The process of translating JS will go like that:        # TOP = 'imports and scope set'

1. Remove all the comments
2. Replace number, string and regexp literals with markers
4. Remove global Functions and move their translation to the TOP. Also add register code there.
5. Replace inline functions with lvals
6. Remove List and Object literals and replace them with lvals
7. Find and remove var declarations, generate python register code that would go on TOP.

Here we should be left with global code only where 1 line of js code = 1 line of python code.
Routine translating this code should be called glob_translate:
1. Search for outer structures and translate them using glob and inside using exps_translate


exps_translate routine:
1. Remove outer {}
2. Split lines at ;
3. Convert line by line using exp_translate
4. In case of error in 3 try to insert ; according to ECMA rules and repeat 3.

exp_translate routine:
It takes a single line of JS code and returns a SINGLE line of Python code.
Note var is not present here because it was removed in previous stages.
If case of parsing errors it must return a pos of error.
1. Convert all assignment operations to put operations, this may be hard :(
2. Convert all gets and calls to get and callprop.
3. Convert unary operators like typeof, new, !, delete.
   Delete can be handled by replacing last get method with delete.
4. Convert remaining operators that are not handled by python eg: === and ,





lval format PyJsLvalNR
marker PyJs(TYPE_NAME)(NR)

TODO
1. Number literal replacement
2. Array literal replacement
3. Object literal replacement
5. Function replacement
4. Literal replacement translators


"""



OP_METHODS = {'*': '__mul__',
              '/': '__div__',
              '%': '__mod__',
              '+': '__add__',
              '-': '__sub__',
              '<<': '__lshift__',
              '>>': '__rshift__',
              '&': '__and__',
              '^': '__xor__',
              '|': '__or__'}

def bracket_split(source, brackets=('()','{}','[]'), strip=False):
    starts = [e[0] for e in brackets]
    in_bracket = 0
    n = 0
    last = 0
    while n<len(source):
        e = source[n]
        if not in_bracket and e in starts:
            in_bracket = 1
            start = n
            b_start, b_end = brackets[starts.index(e)]
        elif in_bracket:
            if e==b_start:
                in_bracket += 1
            elif e==b_end:
                in_bracket -= 1
                if not in_bracket:
                    if source[last:start]:
                        yield source[last:start]
                    last = n+1
                    yield source[start+strip:n+1-strip]
        n+=1
    if source[last:]:
        yield source[last:]

def argsplit(args):
    """used to split JS args (it is not that simple as it seems because
       comma can be inside brackets. Used also to parse array and object elements, and more"""
    parsed_len  = 0
    last = 0
    splits = []
    for e in bracket_split(args, brackets=['()', '[]', '[]']):
        if e[0] not in {'(', '[', '{'}:
            for i, char in enumerate(e):
                if char==',':
                    splits.append(args[last:parsed_len+i])
        parsed_len += len(e)
    return splits

def split_add_ops(text):
    """Specialized function splitting text at add/sub operators.
    Operands are *not* translated. Example result ['op1', '+', 'op2', '-', 'op3']"""
    n = 0
    text = text.replace('++', '##').replace('--', '@@') #text does not normally contain any of these
    spotted = False # set to true if noticed anything other than +- or white space
    last = 0
    while n<len(text):
        e = text[n]
        if e=='+' or e=='-':
            if spotted:
                yield text[last:n].replace('##', '++').replace('@@', '--')
                yield e
                last = n+1
                spotted = False
        elif e=='/' or e=='*' or e=='%':
            spotted = False
        elif e!=' ':
            spotted = True
        n+=1
    yield text[last:n].replace('##', '++').replace('@@', '--')


def split_at_any(text, lis, translate=False, not_before=[], not_after=[]):
    """ doc """
    lis.sort(key=lambda x: len(x), reverse=True)
    last = 0
    n = 0
    text_len = len(text)
    while n<text_len:
        if any(text[:n].endswith(e) for e in not_before):  #Cant end with end before
            n+=1
            continue
        for e in lis:
            s = len(e)
            if s+n>text_len:
                continue
            if any(text[n+s:].startswith(e) for e in not_after):  #Cant end with end before
                n+=1
                break
            if e==text[n:n+s]:
                yield text[last:n] if not translate else translate(text[last:n])
                yield e
                n+=s
                last = n
                break
        else:
            n+=1
    yield text[last:n] if not translate else translate(text[last:n])

def split_at_single(text, sep, not_before=[], not_after=[]):
    """Works like text.split(sep) but separated fragments
    cant end with not_before or start with not_after"""
    n = 0
    lt, s= len(text), len(sep)
    last = 0
    while n<lt:
        if not s+n>lt:
            if sep==text[n:n+s]:
                if any(text[last:n].endswith(e) for e in not_before):
                    pass
                elif any(text[n+s:].startswith(e) for e in not_after):
                    pass
                else:
                    yield text[last:n]
                    last = n+s
                    n += s-1
        n+=1
    yield text[last:]