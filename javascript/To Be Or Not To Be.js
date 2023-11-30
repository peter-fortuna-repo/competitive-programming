// Link to problem: https://leetcode.com/problems/to-be-or-not-to-be

var expect = function(val1) {
    return {
        toBe: (val2) => {
            if (val1 === val2) {
                return true;
            } 
            throw Error("Not Equal");
        },
        notToBe: (val2) => {
            if (val1 !== val2) {
                return true;
            }
            throw Error("Equal");
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */