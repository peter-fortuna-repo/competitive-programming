# You are given an integer array cost where cost[i] is the cost of ith step on
# a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.


# Solution: 
# This problem can be solved using a memoised top down solution. 

# Time complexity: O(n) 
# Space complexity: O(n)

def minCostClimbingStairs(self, cost: List[int]) -> int:
    cost.insert(0,0)
    memo = dict()
    memo[0] = 0
    memo[1] = cost[-1]
    return self.helper(cost, memo)

def helper(self, cost, memo):
    n = len(cost)
    if n in memo:
        return memo[n]
    memo[n] = min(cost[0] + self.helper(cost[1:], memo),
                    cost[0] + self.helper(cost[2:], memo))
    return memo[n]    