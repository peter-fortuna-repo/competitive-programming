// Link to problem: https://leetcode.com/problems/chunk-array

// Solution 1:
var chunk = function(arr, size) {
    let result = [];
    var i=0;
    while(i<arr.length){
        next_chunk = []
        for(var j=i; j<i+size && j<arr.length; j++){
            next_chunk.push(arr[j]);
        }
        result.push(next_chunk);
        i += size;
    }
    return result;
};

// Solution 2:
var chunk = function(arr, size) {
    let result = [];
    let i = 0;
    while(i < arr.length){
        result.push(arr.slice(i, i+size));
        i += size;
    }
    return result;
};