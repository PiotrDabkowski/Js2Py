import js2py
c = js2py.EvalJs()
# c.execute('a = {d:4,f:function k() {return 1}}')
# c.execute('function k(a) {console.log(a);console.log(this)}')
# c.execute('f = function (){}')
a = """
var myFish = ['angel', 'clown', 'mandarin', 'surgeon'];

// removes 0 elements from index 2, and inserts 'drum'
var removed = myFish.splice(2, 0, 'drum');
console.log(myFish)
console.log(removed)
console.log('')
// myFish is ['angel', 'clown', 'drum', 'mandarin', 'surgeon']
// removed is [], no elements removed

// removes 1 element from index 3
removed = myFish.splice(3, 1);
console.log(myFish)
console.log(removed)
console.log('')
// myFish is ['angel', 'clown', 'drum', 'surgeon']
// removed is ['mandarin']

// removes 1 element from index 2, and inserts 'trumpet'
removed = myFish.splice(2, 1, 'trumpet');
console.log(myFish)
console.log(removed)
console.log('')
// myFish is ['angel', 'clown', 'trumpet', 'surgeon']
// removed is ['drum']

// removes 2 elements from index 0, and inserts 'parrot', 'anemone' and 'blue'
removed = myFish.splice(0, 2, 'parrot', 'anemone', 'blue');
console.log(myFish)
console.log(removed)
console.log('')
// myFish is ['parrot', 'anemone', 'blue', 'trumpet', 'surgeon']
// removed is ['angel', 'clown']

// removes 2 elements from index 3
removed = myFish.splice(3, Number.MAX_VALUE);
console.log(myFish)
console.log(removed)
console.log('')
// myFish is ['parrot', 'anemone', 'blue']
// removed is ['trumpet', 'surgeon']

"""
#c.execute(a)
#print c.console()
print js2py.translate_js(a)