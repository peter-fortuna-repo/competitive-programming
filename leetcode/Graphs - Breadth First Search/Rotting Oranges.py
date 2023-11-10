# Link to problem: https://leetcode.com/problems/rotting-oranges

# Solution: 
# We first find all the rotten oranges and put them in a list. Then we iterate 
# through the list and find all the oranges that will rot in the next minute 
# and add them to a new list. We repeat this process until there are no more 
# oranges that will rot in the next minute. If there are still oranges that are
# not rotten, we return -1. Otherwise, we return the number of minutes it took
# to rot all the oranges.

# Time complexity: O(n^2)  
# Space complexity: O(n^2) 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        just_rotted = []
        unfinished = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    unfinished = True
                if grid[i][j] == 2:
                    just_rotted.append((i,j))
        
        time = 0
        if not unfinished:
            return time

        while just_rotted:
            next_layer = []
            for rotten_orange in just_rotted:
                for i, j in [(-1,0), (0,-1), (1,0), (0,1)]:
                    row, col = rotten_orange[0] + i, rotten_orange[1] + j 
                    if (row >= 0 and row < m and
                        col >= 0 and col < n and 
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        next_layer.append((row, col))

            just_rotted = next_layer
            if just_rotted:
                time += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time