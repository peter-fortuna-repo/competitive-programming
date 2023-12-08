// Link to problem: https://leetcode.com/problems/function-composition

var compose = function(functions) {
    
	return function(x) {
        var result = x;
        for (f of functions.reverse()){
            result = f(result);
        }
        return result;
    }
};