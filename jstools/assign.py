
def PyJsAssign(lval, value, scope=None):
    '''Assaigns value to lval in scope and *returns value*.'''
    if isinstance(lval, basestring):
        scope[lval] = value
    else:
        pass
    return value
    
if 1:
	1
	while 1:
	    for x in range(_+1, _*3):
		x