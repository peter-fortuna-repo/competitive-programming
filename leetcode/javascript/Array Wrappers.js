// Link to problem: https://leetcode.com/problems/array-wrappers

/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    var value = 0;
    for (const num of this.nums){
        value += num;
    }
    return value;
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    var str = "[";
    for (const num of this.nums){
        str += num.toString() + ",";
    }
    if (str != "["){
        str = str.substring(0,str.length - 1)
    }
    return str + "]"
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */