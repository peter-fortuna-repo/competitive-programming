# Link to problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

# Solution: Bottom up
# This solution is based on the idea that each day, you can be in one of two 
# states: you either have a stock, or you don't. It tracks the optimal profit 
# for each state, and updates it based on the previous day's optimal profit.

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        stockState, noStockState = -prices[0], 0
        for i in range(1, len(prices)):
            stockState, noStockState = max(stockState, noStockState - prices[i]), max(noStockState, stockState + prices[i] - fee)
        return noStockState