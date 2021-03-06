// Copyright (c) 2012 Ecma International.  All rights reserved.
// Ecma International makes this code available under the terms and conditions set
// forth on http://hg.ecmascript.org/tests/test262/raw-file/tip/LICENSE (the
// "Use Terms").   Any redistribution of this code must retain the above
// copyright and this notice and otherwise comply with the Use Terms.

/*---
es5id: 15.4.4.18-7-9
description: >
    Array.prototype.forEach - modifications to length don't change
    number of iterations
includes: [runTestCase.js]
---*/

function testcase() {

        var called = 0;
        function callbackfn(val, idx, obj) {
            called++;
        }

        var obj = { 1: 12, 2: 9, length: 2 };

        Object.defineProperty(obj, "0", {
            get: function () {
                obj.length = 3;
                return 11;
            },
            configurable: true
        });

        Array.prototype.forEach.call(obj, callbackfn);
        return 2 === called;
    }
runTestCase(testcase);
