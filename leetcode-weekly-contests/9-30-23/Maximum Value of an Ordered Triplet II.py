# Solution: Lookup for Max K and Max i
# Similar to the solution for problem I, except we use an additional list for i
# which allows us to determine i and k based on j. This allows us to find the
# optimal solution in one pass through nums.

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_k = [nums[-1]] * len(nums)
            
        for i in range(len(nums)-2, 0, -1): # from n-2 to 1
            max_k[i] = max(max_k[i+1], nums[i])
        
        max_i = [nums[0]] * len(nums)
        
        for i in range(1, len(nums)-2):
            max_i[i] = max(max_i[i-1], nums[i])
        
        max_value = 0
        for j in range(1, len(nums)-1):
            if max_i[j-1] - nums[j] > 0:
                max_value = max((max_i[j-1] - nums[j]) * max_k[j+1], max_value)
        
        return max_value