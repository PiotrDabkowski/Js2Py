Development in progress...


Now fully supports a very small subset of JavaScript:
1. Expressions
2. Number and String literals

So for example: 
typeof 1 + (1).toString.toString +true

Is translated to rather messy:
PyJsAdd(PyJsAdd(Js(1).typeof(),(Js(1)).get('toString').get('toString')),var.get('true'))

What in turn evalutes to:
numberfunction toString() { [native code] }true

You can run pyjs.py to check out other results:
python pyjs.py 

I think most of the features of JS will be supported by the end of next week (22.11.2014)

