# You can import any compatible node module, similar to npm install module & require(module) in node
from js2py import require

# This will automatically install and translate everything. Subsequent requires are fast because translation is cached.
random_int = require('random-int') # https://www.npmjs.com/package/random-int

print(random_int)
print(random_int(10, 40))
