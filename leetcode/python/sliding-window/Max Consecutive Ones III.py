# Link to problem: https://leetcode.com/problems/max-consecutive-ones-iii

# Solution: This solution uses two pointers to track sequences of consecutive
# ones with at most k 0s in the sequence. The longest sequence is returned.

# Time complexity: O(n) 
# Space complexity: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        num_flips = 0
        l = 0
        p1 = 0
        p2 = 0

        while p2 < len(nums):
            if nums[p2] == 0 and num_flips < k:
                num_flips += 1
            elif nums[p2] == 0 and num_flips == k:
                while nums[p1] == 1:
                    l -= 1
                    p1 += 1
                l -= 1
                p1 += 1

            l += 1
            max_len = max(l, max_len)
            p2 += 1
        
        return max_len