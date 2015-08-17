ES5Harness = {registerTest : function (t) {
    result = t;
    result.problem = false;
    if (t.precondition) {
        try {
            if (t.precondition()===true) {
                result.preconditionResult = 'PASSED'
            } else {
                result.preconditionResult = 'FAILED'
                result.problem = true
            }
        } catch (e) {
            result.precondition = 'ERROR in precondition check ' + e
            result.problem = true
        }
    } else {
        result.preconditionResult = 'No precondition'
    }
    try {
        if (t.test() === true) {
            // report passed
            result.result = 'PASSED'
        } else {
            // report failed
            result.result = 'FAILED'
            result.problem = true
        }
    } catch (e) {
        result.result = 'ERROR: ' + e
        result.problem = true
    }
    return result
}
}

function fnExists(f) {
  if (typeof(f) === "function") {
    return true;
  }
}

var supportsStrict = undefined;
function fnSupportsStrict() {
   "use strict";
   if (supportsStrict!==undefined) return supportsStrict;
   try {eval('with ({}) {}'); supportsStrict=false;} catch (e) {supportsStrict=true;};
   return supportsStrict;
  }

function fnGlobalObject() {
  return (function () {return this}).call(null);
  }


function compareArray(aExpected, aActual) {
  if (aActual.length != aExpected.length) {
    return false;
  }

  aExpected.sort();
  aActual.sort();

  var s;
  for (var i = 0; i < aExpected.length; i++) {
    if (aActual[i] != aExpected[i]) {
      return false;
    }
  }

  return true;
}