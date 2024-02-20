// Link to problem: https://leetcode.com/problems/compact-object

var compactObject = function(obj) {
    if (obj === null) return null;
    if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
    if (typeof obj !== "object") return obj;

    let result = {};
    for (const key in obj){
        let value = compactObject(obj[key]);
        if(value) result[key] = value;
    }
    return result;
};