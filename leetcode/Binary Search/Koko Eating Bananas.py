# Link to problem: https://leetcode.com/problems/koko-eating-bananas


# Solution: 
# This approach checks that Koko can finish for increasing values of k. To find
# k more efficiently than looping through all possible values, the value of k 
# is repeatedly doubled using variation of binary search. This results in a 
# logarithmic number of calls to self.canFinish()

# Time complexity: O(nlog(k)) 
# Note that k is unknown before running this algorithm. However, we get a more
# concrete bound on runtime knowing that k <= max(piles). This comes from the
# fact for k=max(piles), each pile would be visited exactly once, which is the
# minimum amount.

# Space complexity: O(1)


import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while not self.canFinish(piles, h, k):
            k *= 2
        
        low = k//2 + 1
        high = k
        while True:
            k = (low + high)//2
            if self.canFinish(piles, h, k):
                high = k
                if k==1 or not self.canFinish(piles, h, k-1):
                    return k
            else:
                low = k+1



    def canFinish(self, piles: List[int], h: int, k: int) -> bool:
        hours_used = 0
        for pile in piles:
            hours_used += math.ceil(pile/k)
            if hours_used > h:
                return False
        return True
        