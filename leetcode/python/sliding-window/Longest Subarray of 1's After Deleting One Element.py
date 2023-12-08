# Link to problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

# Solution: This solution uses two pointers to track the length of the current
# sequence and check all possible sequences in one pass through nums. The 
# longest sequence is returned.

# Time complexity: O(n) 
# Space complexity: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_ones = 0
        max_ones = 0
        p1 = 0
        p2 = 0

        while p2 < len(nums) and nums[p2] == 1:
            num_ones += 1
            p2 += 1

        if p2 == len(nums):
            return num_ones - 1

        max_ones = max(num_ones, max_ones)
        p2 += 1
        
        while p2 < len(nums):
            if nums[p2] == 0:
                while nums[p1] == 1:
                    p1 += 1
                    num_ones -= 1
                p1 += 1

            if nums[p2] == 1:
                num_ones += 1
            max_ones = max(num_ones, max_ones)
            p2 += 1

        return max_ones