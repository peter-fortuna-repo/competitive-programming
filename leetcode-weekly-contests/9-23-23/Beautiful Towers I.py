# You are given a 0-indexed array maxHeights of n integers.

# You are tasked with building n towers in the coordinate line. The ith tower
# is built at coordinate i and has a height of heights[i].

# A configuration of towers is beautiful if the following conditions hold:

# 1 <= heights[i] <= maxHeights[i]
# heights is a mountain array.
# Array heights is a mountain if there exists an index i such that:

# For all 0 < j <= i, heights[j - 1] <= heights[j]
# For all i <= k < n - 1, heights[k + 1] <= heights[k]
# Return the maximum possible sum of heights of a beautiful configuration of 
# towers.

# 1 <= n == maxHeights <= 10^3
# 1 <= maxHeights[i] <= 10^9


# Solution: Brute force 
# We create the maximum possible height "beautfiul tower" for each peak. This
# solution takes O(n^2) time, which is acceptable given the input array is at 
# most 10^3 entries long.

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maximum_sum = 0
        for i in range(len(maxHeights)):
            maximum_sum = max(self.getMaxAt(maxHeights, i), maximum_sum)
        return maximum_sum
            
    def getMaxAt(self, maxHeights, peak):
        height = maxHeights[peak]
        height_sum = 0
        for i in range(peak, len(maxHeights)):
            height = min(maxHeights[i], height)
            height_sum += height
        
        height = maxHeights[peak]
        for i in range(peak-1, -1, -1):
            height = min(maxHeights[i], height)
            height_sum += height    
        
        return height_sum