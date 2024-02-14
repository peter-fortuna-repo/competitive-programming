// Link to problem: https://leetcode.com/problems/join-two-arrays-by-id

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const merged = {};
    for (e of arr1){
        const id = e.id;
        merged[id] = e;
    }

    for (e of arr2){
        const id = e.id;
        if (!merged[id]){
            merged[id] = e;
        }
        else{
            merged[id] = {...merged[id], ...e};
        }
    }


    const joinedArray = Object.values(merged);
    joinedArray.sort((a, b) => a.id - b.id);

    return joinedArray;
};