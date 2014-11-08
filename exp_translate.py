

def translate_exp(exp):
    '''exp is a string ( in case of valid JS syntax- it is 
    without auto ; insterion - it represents one line of js code )
    returns a string(s) of python code. String*s* because it can return more than
    one if it deduces that exp must consist of more than one line of code'''
    in_par = 0
    in_spar = 0
    while n<len(exp):
        e = exp[n]
        if e=='(':
            if not in_par:
                start_par = n
            in_par+=1
        if e==')' or e=='