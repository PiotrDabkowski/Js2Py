""" This module is still experimental! It has a lot of bugs and host/constructor objects are not implemented yet.
"""

from translators.translator import translate_js


class EvalJs:
    def __init__(self, context=None):
        self.context = {}
        self.__started = False

    def execute(self, js):
        """executes javascript js in current context"""
        if not self.__started:
            code = translate_js(js)
            self.__started = True
        else:
            code = translate_js(js, '')
        exec code in self.context

    def get_variable(self, var):
        """returns variable from global JS context"""
        return self.context['var'].get(var)

    def __getitem__(self, var):
        return self.get_variable(var)
    
e = EvalJs()
x = '''function lcs(string1, string2){
	var longestCommonSubstring = 0;
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
}'''.replace('\t', '\n')

e.execute(x)
print e['lcs']('absdsa','cccccccccccccbsjdcccc')

