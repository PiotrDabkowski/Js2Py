from definitions import *

##################################
StringName = 'PyJsStringCont%d_'
RegExpName = 'PyJsRegExpConst%d_'
##################################

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
    source+='\n'
    comments = []
    inside_comment, single_comment = False, False
    inside_single, inside_double = False, False
    inside_regexp = False
    regexp_class_count = 0
    for n in xrange(len(source)):
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
                        continue
                    if char=='[':
                        regexp_class_count += 1
                    elif char==']':
                        regexp_class_count = max(regexp_class_count-1, 0)
                    elif  char=='/' and not regexp_class_count:
                        quiting_regexp = True 
                else:
                    if char not in alphas+nums+'$_':
                        inside_regexp[1] = n
                        comments.append(inside_regexp)
                        inside_regexp = False
            else:
                if char=='/' and source[n-1]=='/':
                    single_comment = True
                    inside_comment = [n-1, None, 1]
                elif char=='*' and source[n-1]=='/':
                    inside_comment = [n-1, None, 1]
                elif char=='/' and source[n+1] not in ('/', '*'):
                    if not _ensure_regexp(source, n): #<- improve this one
                        continue #Probably just a division 
                    quiting_regexp = False
                    inside_regexp = [n, None, 2]
                    
    res = ''
    start = 0
    count = 0
    constants = {}
    for end, next_start, typ in comments:
          res += source[start:end]
          if typ==0: # String
              count+=1
              name = StringName % count
              res += name
              constants[name] = source[end: next_start]
          elif typ==2:
              count+=1
              name = RegExpName % count
              res += name
              constants[name] = source[end: next_start]
          start = next_start
    res+=source[start:]
    return res.strip(), constants
    
    
def recover_constants(py_source, replacements): #now has n^2 complexity. improve to n
    '''Converts identifiers representing Js constants to the PyJs constants
    PyJsNumberConst_1_ which has the true value of 5 will be converted to PyJsNumber(5)'''
    for identifier, value in replacements.iteritems():
        if 'String' in identifier:
            py_source = py_source.replace(identifier, value)
        elif 'RegExp' in identifier:
            py_source = py_source.replace(identifier, value)
    return py_source
    




#####TEST######

if __name__=='__main__':
    with open('jq.js') as f:
        jq = f.read()

    test = ('regexp_test = /fkf*dsj[/df[[d/*d]/]d*s/*ds]fdf\/fdf*/test;'
            '//some comment"some pseudo string" as \'another pseudo string\' \n'
            'string_test = "fd\'fds[]44343fdsf\\"fs\\"df" //fdfd\n'
            'num_test = 404395493.323e9 //Num to const not supported yet \n'
            '/* another comment 434 /pseudo regex/ ddf */'
            'another_pseudo_regex = 49/4443/323/t[3/5/22+53/23]+f(5/3+r[4/3])+f(/fdd[/]fdf\[/)'
            )
            
    t, d = remove_constants(test)

    print t
    print
    for i, v in d.iteritems():
        print i
        print
        print v
        print 30*'-'

    t, d = remove_constants(jq)

    print t
    print
    import time
 
    time.sleep(10)
    for i, v in d.iteritems():
        print i
        print
        print v
        print 30*'-'
    


