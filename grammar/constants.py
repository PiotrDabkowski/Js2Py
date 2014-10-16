from definitions import *


with open('jq.js') as f:
    jq = f.read()

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
    markers = '(+=[%!*^|&-,;/\\'
    k = 0
    while True:
        k+=1
        if n-k<0:
            return True
        char = source[n-k] 
        if char in markers:
            return True
        if char!=' ':
            break
    return False
    
def remove_comments(source):
    '''Replaces Strings and Numbers in the source code with
       identifier and *removes comments*. Identifier is of the format:
       
       PyJsStringConst_(String const number)_ - for Strings
       PyJsNumberConst_(Number const number)_ - for Numbers

       Returns dict which relates identifier and replaced constant.

       One of the final steps of code translation should be replacing the const identifires with
       their PyJs values.(this is done by recover_constants function) For example:
       var x = 3 will be translated by this function to var x = PyJsNumberConst_1_
       and later by JS to Py translator it will be translated to the python code:
       x = PyJsNumberConst_1_
       But PyJsNumberConst_1_ is simply 3(javascript type) which is represented 
       by PyJsNumber(3) python type
       so the final result is
       x = PyJsNumber(3)
    
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
                if char=='/' and source[n+1] not in ('/', '*'):
                    if not _ensure_regexp(source, n): #<- improve this one
                        continue #Probably just a division 
                    quiting_regexp = False
                    inside_regexp = [n, None, 2]
                    
    res = ''
    start = 0
    count = 0
    StringName = 'PyJsStringCont%d_'
    count = 0
    RegExpName = 'PyJsRegExpConst%d_'
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
    
    
    
def recover_constants(py_source, replacements):
    '''Converts identifiers representing Js constants to the PyJs constants
    PyJsNumberConst_1_ which has the true value of 5 will be converted to PyJsNumber(5)'''
    for identifier, value in replacements.iteritems():
        if 'String' in identifier:
            py_source = py_source.replace(identifier, value)
        elif 'RefExp' in identifier:
            py_source = py_source.replace(identifier, value)
    return py_source
    
    
    
#def remove_constants(source):
#    
#    #Remove comments from the source
#    source = remove_comments(source)
#    
#    #Prepare global variables
#    global StringNr, NumberNr, replacements
#    StringNr = 0
#    NumberNr = 0
#    replacements = {}
#
#    #STRING
#    def string_replace(string): #Replacing function
#        global StringNr, replacements
#        StringNr+=1
#        identifier = 'PyJsStringConst_%d_'%(StringNr)
#        replacements[identifier] = string[0]
#        return identifier
#    
#    str_rep = StringLiteral.copy().setParseAction(string_replace) 
#    source = str_rep.transformString(source) #Done
#
#    #NUMBER
#    def number_replace(number):  #Replacing function
#        global NumberNr, replacements
#        NumberNr+=1
#        identifier = 'PyJsNumberConst_%d_'%(NumberNr)
#        replacements[identifier] = number[0][0]
#        return identifier
#    num_rep = NumericLiteral.copy().setParseAction(number_replace) 
#    source = num_rep.transformString(source) #Done
#    
#    return source, replacements


    
t, d = remove_comments(jq)
for e in sorted({}):
    if len(d[e])<200:
        continue
    print 
    print e
    print 
    print
    print d[e]
