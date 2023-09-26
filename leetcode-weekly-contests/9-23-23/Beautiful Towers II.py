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

# 1 <= n == maxHeights <= 10^5
# 1 <= maxHeights[i] <= 10^9


# Solution: Towards optimization
# Two things to note 
# - This problem is identical to Beautiful towers I with the maximum size
#   bumped up from 10^3 to 10^5
# - While my optimization method should work, I was unable to finish the 
#   algorithm during the contest time. This is my incomplete solution.
# 
# My method tracks bottlenecks to avoid looping through every element in the 
# "getMaxAt" step. The worst case is still the same, but typical cases are 
# signifigantly faster, especially for larger inputs.

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maximum_sum = 0
        bottlenecks = []
        for i in range(len(maxHeights)):
            if i % 500 == 0:
                bottlenecks, peak_index = self.findBottlenecks(maxHeights, i)
            if i > bottlenecks[peak_index][0]:
                peak_index += 1
            
            maximum_sum = max(self.getMaxAt(maxHeights, i, bottlenecks, peak_index), maximum_sum)
        
        return maximum_sum
            
    def findBottlenecks(self, maxHeights, peak):
        bottlnecks = [maxHeights[peak]]
        height = maxHeights[peak]
        for i in range(peak, len(maxHeights)):
            if maxHeights[i] < height:
                height = maxHeights[i]
                bottlenecks.append((i, height))
        
        peak_index = 0
        height = maxHeights[peak]
        for i in range(peak-1, -1, -1):
            if maxHeights[i] < height:
                height = maxHeights[i]
                bottlenecks.insert(0,(i,height))
                peak_index += 1
            
        return bottlenecks, peak_index
        
    def getMaxAt(self, maxHeights, peak, bottlenecks, peak_index):
        height_sum = 0
        height = maxHeights[peak]
        bottleneck_index = peak_index
        while height > bottlenecks[bottleneck_index][1]:
            
        for i, bottleneck in enumerate(bottlenecks[bottleneck_index:-2]):
            height_sum += bottleneck[1] * (bottlenecks[bottleneck_index + i+1][0] - bottleneck[0])
            
        
        for i, bottleneck in enumerate(bottlenecks[bottleneck_index:1:-1]):
            height_sum += bottleneck[1] * (bottleneck[0] - bottleneck)
        
        
        return height_sum