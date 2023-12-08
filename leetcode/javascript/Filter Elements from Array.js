// Link to problem: https://leetcode.com/problems/filter-elements-from-array

var filter = function(arr, fn) {
    var filteredArr = [];
    arr.map(fn).forEach( function (item, index){
        if (item){
            filteredArr.push(arr[index]);
        }
    });
    return filteredArr;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */