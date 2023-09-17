# You are given a 0-indexed integer array nums and an integer k.
# Return an integer that denotes the sum of elements in nums whose 
# corresponding indices have exactly k set bits in their binary representation.

# Solution: 
# We simply loop through each index and check the number of 1s in its binary
# representation.

# Time complexity: O(n)
# Space complexity: O(1)

def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
    sum = 0
    for i, num in enumerate(nums):
        if self.hasKBits(i, k):
            sum += num
    return sum

def hasKBits(self,num, k):
    count = 0
    while num:
        if num & 1:
            count += 1
        if count > k:
            return False
        num = num >> 1      
    if count < k:
        return False
    return True