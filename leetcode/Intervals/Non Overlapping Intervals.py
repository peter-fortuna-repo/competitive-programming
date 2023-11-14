# Link to problem: https://leetcode.com/problems/non-overlapping-intervals

# Solution:
# We first sorth the intervals by their end time. Then we iterate through the 
# intervals and keep track of the end time of the last interval we added. If
# the start time of the current interval is less than the end time of the last
# interval, num_removed is incremented.

# Time complexity: O(nlog(n))
# Space complexity: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = [interval[::-1] for interval in intervals]
        intervals.sort()
        start_time = -5 * 10**4
        num_removed = 0

        for interval in intervals:
            if interval[1] >= start_time:
                start_time = interval[0]
            else:
                num_removed += 1
        return num_removed