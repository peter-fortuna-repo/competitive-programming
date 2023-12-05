// Link to problem: https://leetcode.com/problems/allow-one-function-call

var once = function(fn) {
    callCount = 0;
	return function(...args){
        if(!callCount){
            callCount += 1;
            return fn(...args);
        }
    }
};