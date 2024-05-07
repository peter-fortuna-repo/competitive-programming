# Link to problem: https://leetcode.com/problems/minimum-cost-to-equalize-array/

# NOTE: Solution is incomplete.

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        max_num = max(nums)
        if cost1 < cost2/2:
            cost = 0
            for num in nums:
                cost += (max_num - num) * cost1
            return cost % (10**9 + 7)

        i = 0
        j = 1
        n = len(nums)
        fill_i = 0
        fill_j = 0
        cost = 0

        while i < n and j < n:
            if nums[i] + fill_i == max_num:
                i = max(i+1, j+1)
            elif nums[j] + fill_j == max_num:
                j = max(i+1, j+1)
            else:
                num_increases = (max_num - max(nums[i] + fill_i, nums[j] + fill_j))
                cost += num_increases * cost2
                if nums[i] + fill_i > nums[j] + fill_j:
                    fill_i = 0
                    fill_j += num_increases
                    i = max(i+1, j+1)
                else:
                    fill_i += num_increases
                    fill_j = max(i+1, j+1)
            
        final_index = min(i,j)
        fill = fill_i if i < j else fill_j
        remainder = max_num - (nums[final_index] + fill)
        cost += cost1 * remainder 
        return cost