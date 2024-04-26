# Link to problem: https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26

# Solution:
# This solution uses a greedy algorithm to find the minimum falling path sum.
# Consider that for each element in a row, the minimum path that ends on that 
# element will be the that element plus the minimum path from the previous row
# that is not in the same column. We can use this property to calculate the 
# minimum path for each possible route in one pass through the grid.

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        optimal_path = grid[0]
        for row in grid[1:]:
            next_row = row
            for i in range(n):
                next_row[i] += min(optimal_path[:i] + optimal_path[i+1:])
            optimal_path = next_row

        return min(optimal_path)

        