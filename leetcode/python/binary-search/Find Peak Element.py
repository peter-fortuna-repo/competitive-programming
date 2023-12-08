# Link to problem: https://leetcode.com/problems/find-peak-element


# Solution: Binary Search
# The trick here is to use a binary search. You can think of the array as an 
# actual mountain - each element is either valley with higher neighbors left 
# and right, a peak with lower neighbors left and right, or a slopes with one 
# neighbor higher and one lower. Critically, the conditions of the problem 
# guarentee that a position is never flat, with a neighbor of equal value. Note
# that the slope either points left or right. If you follow the direction of 
# the slope binary search style, you will find a peak.

# Time complexity: O(log(n)) 
# Space complexity: O(1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        if high == 0:
            return high
        if nums[low] > nums[low+1]:
            return low
        if nums[high] > nums[high-1]:
            return high
        
        while True:
            mid = (low+high)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                low = mid
            else:
                high = mid