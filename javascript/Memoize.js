// Link to problem: https://leetcode.com/problems/memoize

function memoize(fn) {
    let memo = {};
    return function(...args) {
        const key = args.toString();
        if(!(key in memo)){
            memo[key] = fn(...args);
        }
        return memo[key];
    }
}