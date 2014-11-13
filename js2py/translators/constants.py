from string import ascii_lowercase, digits
##################################
StringName = 'PyJsConstantString%d_'
NumberName = 'PyJsConstantNumber%d_'
RegExpName = 'PyJsConstantRegExp%d_'
##################################
ALPHAS = set(ascii_lowercase+ ascii_lowercase.upper())
NUMS = set(digits)
IDENTIFIER_START = ALPHAS.union(NUMS)
HEX = set('0123456789abcdefABCDEF')
from utils import IDENTIFIER_PART
IDENTIFIER_PART  = IDENTIFIER_PART.union({'.'})


def _is_cancelled(source, n):
    cancelled = False
    k = 0
    while True:
        k+=1
        if source[n-k]!='\\':
            break
        cancelled = not cancelled
    return cancelled
    
def _ensure_regexp(source, n): #<- this function has to be improved
    '''returns True if regexp starts at n else returns False
      checks whether it is not a division '''
    markers = '(+~"\'=[%!*^|&-,;/\\'
    k = 0
    while True:
        k+=1
        if n-k<0:
            return True
        char = source[n-k] 
        if char in markers:
            return True
        if char!=' ' or char!='\n':
            break
    return False

def parse_num(source, start, charset):
    """Returns a first index>=start of chat not in charset"""
    while source[start] in charset:
        start+=1
    return start

def parse_exponent(source, start):
    """returns end of exponential, raises SyntaxError if failed"""
    if not source[start] in {'e', 'E'}:
        if source[start] in IDENTIFIER_PART:
            raise SyntaxError('Invalid number literal!')
        return start
    start += 1
    if source[start] in {'-', '+'}:
        start += 1
    FOUND = False
    # we need at least one dig after exponent
    while source[start] in NUMS:
        FOUND = True
        start+=1
    if not FOUND or source[start] in IDENTIFIER_PART:
        raise SyntaxError('Invalid number literal!')
    return start

def remove_constants(source):
    '''Replaces Strings and Regexp literals in the source code with
       identifiers and *removes comments*. Identifier is of the format:
       
       PyJsStringConst(String const number)_ - for Strings
       PyJsRegExpConst(RegExp const number)_ - for RegExps

       Returns dict which relates identifier and replaced constant.
    
       Removes single line and multiline comments from JavaScript source code
       Pseudo comments (inside strings) will not be removed.

       For example this line:
       var x = "/*PSEUDO COMMENT*/ TEXT //ANOTHER PSEUDO COMMENT"
       will be unaltered'''
    source=' '+source+'\n'
    comments = []
    inside_comment, single_comment = False, False
    inside_single, inside_double = False, False
    inside_regexp = False
    regexp_class_count = 0
    n = 0
    while n < len(source):
        char = source[n]
        if char=='"' and not (inside_comment or inside_single or inside_regexp):
            if not _is_cancelled(source, n):
                if inside_double:
                    inside_double[1] = n+1
                    comments.append(inside_double)
                    inside_double = False
                else:
                    inside_double = [n, None, 0]
        elif char=="'"  and not (inside_comment  or inside_double or inside_regexp):
            if not _is_cancelled(source, n):
                if inside_single:
                    inside_single[1] = n+1
                    comments.append(inside_single)
                    inside_single = False
                else:
                    inside_single = [n, None, 0]
        elif not (inside_single or inside_double):
            if inside_comment:
                if single_comment:
                    if char=='\n':
                        inside_comment[1] = n
                        comments.append(inside_comment)
                        inside_comment = False
                        single_comment = False
                else: # Multiline
                    if char=='/' and source[n-1]=='*':
                        inside_comment[1] = n+1
                        comments.append(inside_comment)
                        inside_comment = False
            elif inside_regexp:
                if not quiting_regexp:
                    if _is_cancelled(source, n):
                        n+=1
                        continue
                    if char=='[':
                        regexp_class_count += 1
                    elif char==']':
                        regexp_class_count = max(regexp_class_count-1, 0)
                    elif  char=='/' and not regexp_class_count:
                        quiting_regexp = True 
                else:
                    if char not in IDENTIFIER_START:
                        inside_regexp[1] = n
                        comments.append(inside_regexp)
                        inside_regexp = False
            elif char=='/' and source[n-1]=='/':
                single_comment = True
                inside_comment = [n-1, None, 1]
            elif char=='*' and source[n-1]=='/':
                inside_comment = [n-1, None, 1]
            elif char=='/' and source[n+1] not in ('/', '*'):
                if not _ensure_regexp(source, n): #<- improve this one
                    n+=1
                    continue #Probably just a division
                quiting_regexp = False
                inside_regexp = [n, None, 2]
            elif not (inside_comment or inside_regexp):
                if 1 and (char in NUMS or char=='.') and source[n-1] not in IDENTIFIER_PART:
                    if char=='.':
                        k = parse_num(source,n+1, NUMS)
                        if k==n+1: # just a stupid dot...
                            n+=1
                            continue
                        k = parse_exponent(source, k)
                    elif char=='0' and source[n+1] in {'x', 'X'}: #Hex number probably
                        k = parse_num(source, n+2, HEX)
                        if k==n+2 or source[k] in IDENTIFIER_PART:
                            raise SyntaxError('Invalid hex literal!')
                    else: #int or exp or flot or exp flot
                        k = parse_num(source, n+1, NUMS)
                        if source[k]=='.':
                            k = parse_num(source, k+1, NUMS)
                        k = parse_exponent(source, k)
                    comments.append((n, k, 3))
                    n = k
                    continue
        n+=1
    res = ''
    start = 0
    count = 0
    constants = {}
    for end, next_start, typ in comments:
          res += source[start:end]
          if typ==0: # String
              name = StringName
          elif typ==1: # comment
              continue
          elif typ==2: # regexp
              name = RegExpName
          elif typ==3: # number
              name = NumberName
          else:
              raise RuntimeError()
          res += name % count
          constants[name % count] = source[end: next_start]
          start = next_start
          count += 1
    res+=source[start:]
    return res.strip(), constants
    
    
def recover_constants(py_source, replacements): #now has n^2 complexity. improve to n
    '''Converts identifiers representing Js constants to the PyJs constants
    PyJsNumberConst_1_ which has the true value of 5 will be converted to PyJsNumber(5)'''
    for identifier, value in replacements.iteritems():
        py_source = py_source.replace(identifier, 'Js(%s)'%value)
    return py_source




#####TEST######

if __name__=='__main__':
    test = (' 0X07 regexp_test = /fkf*dsj[/df[[d/*d]/]d*s/*ds]fdf\/fdf*/test;'
            '//some comment"some pseudo string" as \'another pseudo string\' \n'
            'string_test .8778e-7 = "fd\'fds[]44343fdsf\\"fs\\"df" //fdfd\n'
            'num_test = 404395493.323e9 //Num to const not supported yet \n'
            '/* another comment 434 /pseudo regex/ ddf .322k */'
            'another_pseudo_regex = 49/4443/323/t[3/5/22+53/23]+f09990(5/3+r[4/k.434])+f(/fdd[/]fdf\[/)'
            )
            
    t, d = remove_constants(test)
    import time
    with open('jq.js') as f:
        jq = f.read()
    print time.time()
    t, d = remove_constants(jq)
    print time.time()
    b = recover_constants(t, d)
    print time.time()