# LInk to problem: https://leetcode.com/problems/online-stock-span


# Solution:
# This solution uses a monotonic stack to track the stock prices and their 
# spans. To determine the span, simply pop off all the prices that are less
# than or equal to the current price and add their spans to the current span.

# Time complexity: O(n) 
# Space complexity: O(n)

class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []        

    def next(self, price: int) -> int:
        span = [price, 1]
        while self.monotonic_stack and price >= self.monotonic_stack[-1][0]:
            span[1] += self.monotonic_stack.pop()[1]
        self.monotonic_stack.append(span)
        return span[1]