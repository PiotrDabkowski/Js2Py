from definitions import *
import random

with open('jq.js') as f:
    jq = f.read()
    
def remove_comments(source):
    '''Removes single line and multiline comments from JavaScript source code
       Pseudo comments (inside strings) will not be removed.

       For example this line:
       var x = "/*PSEUDO COMMENT*/ TEXT //ANOTHER PSEUDO COMMENT"
       will be unaltered'''
    source+='\n'
    comments = []
    inside_comment, single_comment = False, False
    inside_single, inside_double = False, False
    for n in xrange(len(source)):
        char = source[n]
        if char=='"' and not inside_comment:
            cancelled = False
            while n:
                n-=1
                if source[n]!='\\':
                    break
                cancelled = not cancelled
            if not inside_single and not cancelled:
                inside_double = not inside_double
        elif char=="'"  and not inside_comment:
            cancelled = False
            while n:
                n-=1
                if source[n]!='\\':
                    break
                cancelled = not cancelled
            if not inside_double and not cancelled:
                inside_single = not inside_single
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
            else:
                if char=='/' and source[n-1]=='/':
                    single_comment = True
                    inside_comment = [n-1, None]
                elif char=='*' and source[n-1]=='/':
                    inside_comment = [n-1, None]
    res = ''
    start = 0
    for end, next_start in comments:
          res+=source[start:end]
          start = next_start
    res+=source[start:]
    return res.strip()

def remove_constants(source):
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
       But PyJsNumberConst_1_ is simply 3(javascript type) which is represented by PyJsNumber(3) python type
       so the final result is
       x = PyJsNumber(3)'''
    #Remove comments from the source
    source = remove_comments(source)
    
    #Prepare global variables
    global StringNr, NumberNr, replacements
    StringNr = 0
    NumberNr = 0
    replacements = {}

    #STRING
    def string_replace(string): #Replacing function
        global StringNr, replacements
        StringNr+=1
        identifier = 'PyJsStringConst_%d_'%(StringNr)#, ''.join(random.choice(alphas) for n in xrange(5)))
        replacements[identifier] = string[0]
        return identifier
    
    str_rep = StringLiteral.copy().setParseAction(string_replace) 
    source = str_rep.transformString(source) #Done

    #NUMBER
    def number_replace(number):  #Replacing function
        global NumberNr, replacements
        NumberNr+=1
        identifier = 'PyJsNumberConst_%d_'%(NumberNr)#, ''.join(random.choice(alphas) for n in xrange(5)))
        replacements[identifier] = number[0][0]
        return identifier
    num_rep = NumericLiteral.copy().setParseAction(number_replace) 
    source = num_rep.transformString(source) #Done
    
    return source, replacements

def recover_constants(py_source, replacements):
    '''Converts identifiers representing Js constants to the PyJs constants
    PyJsNumberConst_1_ which has the true value of 5 will be converted to PyJsNumber(5)'''
    for identifier, value in replacements.iteritems():
        if 'String' in identifier:
            py_source = py_source.replace(identifier, 'PyJsString(%s)'%value)
        else:
            py_source = py_source.replace(identifier, 'PyJsNumber(%s)'%value)
    return py_source
    

