# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements. Perform this operation in place.

# Solution 1: 
# We keep one pointer at the leftmost zero and swap this value with the 
# leftmost non-zero value. This solution is innefficient, as you needlessly
# move the same zeros multiple times.

# Computational complexity: O(n^2)
# Space complexity: O(1)
 

def moveZeroes(self, nums: List[int]) -> None:
    n = len(nums)
    if n == 1: return

    p1 = 0
    p2 = 1

    while p1 < n:
        while nums[p1] != 0:
            p1 += 1
            if p1 == n: return
        
        p2 = p1
        while nums[p2] == 0:
            p2 += 1
            if p2 == n: return
        
        nums[p1] = nums[p2]
        nums[p2] = 0


# Solution 2: 
# We start by counting the number of zeros in our list. Using two pointers, we
# only move nonzero numbers. At the end, we replace the remaining spaces with 
# 0s. This allows us to move all zeros in two passes or less.

# Computational complexity: O(n)
# Space complexity: O(1)

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        num_zeros = nums.count(0)

        if n == 1 or num_zeros == 0:
            return
        
        p1, p2 = 0, 0

        while p1 < n - num_zeros:
            while nums[p2] == 0:
                p2 += 1
            
            nums[p1] = nums[p2]
            p1 += 1
            p2 += 1


        for i in range(n-num_zeros, n):
            nums[i] = 0

        return

# Computational complexity: O(n)

