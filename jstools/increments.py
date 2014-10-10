
def PyJsPreIncrement(name, local={}):
	if name in local:
		local[name]+=1
		return local[name]
	globals()[name]+=1
	return globals()[name]

def PyJsPostIncrement(name, local={}):
	if name in local:
		local[name]+=1
		return local[name]-1
	globals()[name]+=1
	return globals()[name]-1

def PyJsPreDecrement(name, local={}):
	if name in local:
		local[name]-=1
		return local[name]
	globals()[name]-=1
	return globals()[name]
    
def PyJsPostDecrement(name, local={}):
	if name in local:
		local[name]-=1
		return local[name]+1
	globals()[name]-=1
	return globals()[name]+1
