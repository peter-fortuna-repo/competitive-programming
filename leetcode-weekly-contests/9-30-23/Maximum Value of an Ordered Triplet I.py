# Solution: Lookup for Max K
# The brute for solution is to use a triple loop and check all the possible 
# combinations. We can speed this up by having a reference for k. In one pass
# from right to left, we can determine the maximum element to the right of any
# index i. This allows us to skip the last loop and lookup the optimal value
# that would have been found in that pass. 

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_k = [nums[-1]] * len(nums)
            
        for i in range(len(nums)-2, 0, -1): # from n-2 to 1
            max_k[i] = max(max_k[i+1], nums[i])
        
        max_value = 0
        for i in range(len(nums)-2):
            for j in range(i, len(nums)-1):
                if nums[i] - nums[j] > 0:
                    max_value = max((nums[i] - nums[j]) * max_k[j+1], max_value)
                # else:
                    # max_value = max((nums[i] - nums[j]) * min_k[j+1], max_value)
        return max_value