// Link to problem: https://leetcode.com/problems/group-by

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const result = {};
    for (e of this){
        const key = fn(e);
        result[key] ||= [];
        result[key].push(e);
    }
    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */