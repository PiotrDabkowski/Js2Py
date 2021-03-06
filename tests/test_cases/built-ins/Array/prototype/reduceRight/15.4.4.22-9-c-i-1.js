// Copyright (c) 2012 Ecma International.  All rights reserved.
// Ecma International makes this code available under the terms and conditions set
// forth on http://hg.ecmascript.org/tests/test262/raw-file/tip/LICENSE (the
// "Use Terms").   Any redistribution of this code must retain the above
// copyright and this notice and otherwise comply with the Use Terms.

/*---
es5id: 15.4.4.22-9-c-i-1
description: >
    Array.prototype.reduceRight - element to be retrieved is own data
    property on an Array-like object
includes: [runTestCase.js]
---*/

function testcase() {

        var testResult = false;
        function callbackfn(prevVal, curVal, idx, obj) {
            if (idx === 0) {
                testResult = (curVal === 0);
            }
        }

        var obj = { 0: 0, 1: 1, 2: 2, length: 2 };
        Array.prototype.reduceRight.call(obj, callbackfn, "initialValue");
        return testResult;
    }
runTestCase(testcase);
