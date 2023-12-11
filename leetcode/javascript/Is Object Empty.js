// Link to problem: https://leetcode.com/problems/is-object-empty

// Solution 1:
var isEmpty = function(obj) {
    return JSON.stringify(obj).length == 2;
};

// Solution 2:
var isEmpty = function(obj) {
    for (var _ in obj){return false;}
    return true;
};