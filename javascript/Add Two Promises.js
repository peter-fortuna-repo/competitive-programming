// Link to problem: https://leetcode.com/problems/add-two-promises

 // Solution 1:
var addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2]).then(([v1, v2]) => v1 + v2);
};


// Solution 2: 
var addTwoPromises = async function(promise1, promise2) {
    const [v1, v2] = await Promise.all([promise1, promise2]);
    return v1 + v2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */