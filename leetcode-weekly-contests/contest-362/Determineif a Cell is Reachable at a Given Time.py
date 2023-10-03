# Link to Problem: https://leetcode.com/contest/weekly-contest-362/problems/determine-if-a-cell-is-reachable-at-a-given-time/

# Solution:
# While the problem may sound complex, it actually has a very simple solution.
# Since you can move diagonally and repeatedly visit tiles, the answer is True
# so long as time t is greater than the length and wigth from start to finish.

# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if(sx == fx and sy == fy and t == 1):
            return False
        if(max(abs(fx - sx), abs(fy - sy)) <= t):
            return True
        return False