###Pure Python JavaScript Translator/Interpreter. 

Still under development prototypes are not fully finished and constructors are not implemented at all. But it can do basic translations. For example let's translate this LongestCommonSubstring algorithm:

    x = '''function longestCommonSubstring(string1, string2){
        	// init max value
        	var longestCommonSubstring = 0;
        	// init 2D array with 0
        	var table = [],
                    len1 = string1.length,
                    len2 = string2.length,
                    row, col;
        	for(row = 0; row <= len1; row++){
        		table[row] = [];
        		for(col = 0; col <= len2; col++){
        			table[row][col] = 0;
        		}
        	}
        	// fill table
                var i, j;
        	for(i = 0; i < len1; i++){
        		for(j = 0; j < len2; j++){
        			if(string1[i]==string2[j]){
        				if(table[i][j] == 0){
        					table[i+1][j+1] = 1;
        				} else {
        					table[i+1][j+1] = table[i][j] + 1;
        				}
        				if(table[i+1][j+1] > longestCommonSubstring){
        					longestCommonSubstring = table[i+1][j+1];
        				}
        			} else {
        				table[i+1][j+1] = 0;
        			}
        		}
        	}
        	return longestCommonSubstring;
        }'''
Here is how to do that:

    >>> from js2py.evaljs import EvalJs
    >>> e = EvalJs()
    >>> e.execute(x) # where x is our longest common subsequence algoritm in JavaScript
    >>> e['lcs']
    function lcs(string1, string2) { [python code] }
    >>> e['lcs']('js2py','pyjs')
    2 
js2py and pyjs have longest common subsequence 'py' which has length 2 so the answer is correct. 







