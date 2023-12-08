// Link to problem: https://leetcode.com/problems/array-reduce-transformation

var reduce = function(nums, fn, init) {
    for (num of nums){
        init = fn(init, num);
    }
    return init;
  };