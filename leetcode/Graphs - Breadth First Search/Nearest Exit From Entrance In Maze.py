# Link to problem: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

# Solution: 
# We start at the entrance and find all possible steps we can take. We then
# mark those steps as visited by changing the value of the cell to '+' and 
# increase the step count by 1. We repeat this process until we reach an exit
# or we run out of steps to take. If an exit is reached, we return the step
# count. If no exit is reached, we return -1.

# Time complexity: O(n^2)  
# Space complexity: O(n^2) 

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n, steps = len(maze), len(maze[0]), 0
        current_routes = [entrance]
        maze[entrance[0]][entrance[1]] = "+"

        while current_routes:
            steps += 1
            next_steps = []
            for route in current_routes:
                for i,j in [(-1,0), (0,-1), (1,0), (0,1)]:
                    row, col = route[0] + i, route[1] + j
                    if (row >= 0 and row < m and
                        col >= 0 and col < n and
                        maze[row][col] == '.'):
                        maze[row][col] = '+'
                        next_steps.append((row, col))
                        if (row == 0 or row == m-1 or
                            col == 0 or col == n-1):
                            return steps

            current_routes = next_steps
            
        return -1