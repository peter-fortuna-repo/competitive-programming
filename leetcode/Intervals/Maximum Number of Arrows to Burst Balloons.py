# Link to problem: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

# Solution:
# This solution is based on the idea that it is always effective to shoot and
# arrow at the left of the rightmost balloon. This is because it will always 
# overlap with the maximum number of balloons. Therefore, we sort the balloons
# and then pop the rightmost balloon and pop all balloons that overlap with it
# until all baloons are popped.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0
        while points:
            arrows += 1
            balloon = points.pop()
            while points and balloon[0] <= points[-1][1]:
                points.pop()
        
        return darts