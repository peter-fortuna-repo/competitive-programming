# Link to problem: https://leetcode.com/problems/equal-row-and-column-pairs

# Solution 1: Brute force
# We check for each possible match between rows and columns. We reconstruct the
# column in each cycle, which saves space but adds runtime.

# Time complexity: O(n^3) 
# Space complexityL O(n)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i] == [grid[k][j] for k in range(n)]:
                    count += 1
        return count

# Solution 2: Store rows 
# We repeat the same process as solution 1, but pre-compute all columns. This
# brings our runtime down to O(n^2) and increases space used to O(n^2).

# Time complexity: O(n^2)
# Space complexityL O(n^2)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        columns = [[grid[k][j] for k in range(n)] for j in range(n)]

        for row in grid:
            for column in columns:
                if row == column:
                    count += 1
        return count

# Solution 3: Hashmap
# We convert each row into a string and store it in a hashmap. This allows us 
# to identify whether strings match in constant time. However, constructing the
# columns still take O(n^2) time, which keeps this algorithm in O(n^2).

# Time complexity: O(n^2)
# Space complexityL O(n^2)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        rows = dict()

        for row in grid:
            if str(row) not in rows:
                rows[str(row)] = 0
            rows[str(row)] += 1

        columns = [[grid[k][j] for k in range(n)] for j in range(n)]
        for column in columns:
            if str(column) in rows:
                count += rows[str(column)]
        
        return count