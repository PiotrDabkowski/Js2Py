import js2py

# there are 2 easy methods to run js file from Js2Py

# Method 1:
eval_result, example = js2py.run_file('example.js')


# Method 2:
js2py.translate_file('example.js', 'example.py') # this translates and saves equivalent Py file
from example import example  # yes, it is: import lib_name from lib_name


##### Now you can use your JS code as if it was Python!

print(example.someVariable)
print(example.someVariable.a)
print(example.someVariable['a'])

example.sayHello('Piotrek!')
example.sayHello()   # told you, just like JS.

example['$nonPyName']()  # non py names have to be accessed through []   example.$ is a syntax error in Py.


# but there is one problem - it is not possible to write 'new example.Rectangle(4,3)' in Python
# so you have to use .new(4,3) instead, to create the object.
rect = example.Rectangle.new(4,3)
print(rect.getArea())  # should print 12
