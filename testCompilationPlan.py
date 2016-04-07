import js2py
import datetime
now = datetime.datetime.now

# the line below will
# - build a 'compilation plan' by substituting strings and constants with placeholders
# - then build the ast and emit the python code from that compilation plan
# - then substitute back in the constants
# This causes some regex overhead, but for js code with similar structure
# subsequent translate_js calls are 20 times faster
js2py.translate_js('name == "Robert" && age == 46', use_compilation_plan=True)

# this lines below will re-use the compilation plan already laid out by the
# statement above
js2py.translate_js('name == "Guido" && age == 50', use_compilation_plan=True)
js2py.translate_js('name == "Spam" && age == 25', use_compilation_plan=True)

# now we'll show off the performance gain:
start = now()
for cnt in range(10000):
	js2py.translate_js('name == "Robert" && age == %i'%cnt, use_compilation_plan=False)
print(('duration without compilation plan %i'%(now() - start).seconds))

start = now()
for cnt in range(10000):
	js2py.translate_js('name == "Robert" && age == %i'%cnt, use_compilation_plan=True)
print(('duration with compilation plan %i'%(now() - start).seconds))

# you can see how a compilation plan works with the lines below:
from js2py.translators.translator import get_compilation_plan
expression = "Age==1 && Gender==2 && JobTitle=='Decision maker'"
strings, numbers, plan = get_compilation_plan(expression)
print('strings:\n%s'%strings)
print('numbers:\n%s'%numbers)
print('plan:\n%s'%plan)
print(js2py.translate_js(expression))
