import pyesprima
f = open('esp.js').read()
print pyesprima
e = pyesprima.parse(f)
print e