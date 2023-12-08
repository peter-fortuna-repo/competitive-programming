# Link to problem: https://leetcode.com/problems/increasing-triplet-subsequence

# Solution 1: Min left, max right
# For this solution, I keep track of the smallest nums[i] could be given j and 
# the largest nums[k] could be given j. This is done in O(n) by moving through 
# nums left to right to track the smallest value, then moving right to left 
# and tracking the largest index. Once this is complete, we can take one pass 
# through all possible values of j and checck if the smallest compatible 
# nums[i] and largest nums[k] meet the problem's requirements. 

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_left_j = [nums[0]] * len(nums)
        max_right_j = [nums[-1]] * len(nums)

        for i in range(1,len(nums)):
            min_left_j[i] = min(min_left_j[i-1], nums[i])

        for k in range(len(nums)-2,1,-1):
            max_right_j[k] = max(max_right_j[k+1], nums[k])
        
        for j in range(1,len(nums)-1):
            if min_left_j[j-1] < nums[j] and nums[j] < max_right_j[j+1]:
                return True
        
        return False


# Solution 2: Constant space
# This problem can be solved in a single pass through nums. Our search looks
# for the final index, k, and keeps track of potential i and j values. Once the
# algorithm finds a k satisfying the problem's criterea, it returns true.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False