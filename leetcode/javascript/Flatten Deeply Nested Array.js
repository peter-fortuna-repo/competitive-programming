// Link to problem: https://leetcode.com/problems/flatten-deeply-nested-array

var flat = function (arr, n) {
    const result = [];
    for(let e of arr){
        if(!Array.isArray(e)){
            result.push(e);
        }
        else{
            e = flat(e, n-1);
            if(n > 0){
                for(let f of e){
                    result.push(f);
                }
            }
            else {
                result.push(e);
            }
        }
    }
    return result;
};