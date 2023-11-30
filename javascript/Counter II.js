// Link to problem: https://leetcode.com/problems/counter-ii

var createCounter = function(init) {
    n = init;
    return {
        increment: () => {
            n += 1.
            return n;
        },
        reset: () => {
            n = init;
            return n;
        },
        decrement: () => {
            n -= 1;
            return n;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */