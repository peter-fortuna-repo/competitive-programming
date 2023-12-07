// Link to problem: https://leetcode.com/problems/intervval-cancellation

var cancellable = function(fn, args, t) {
    const cancelFn = () => {clearInterval(repeatingFn)};
    fn(...args);
    const repeatingFn = setInterval(() => fn(...args), t);
    return cancelFn;
};
