# Link to problem: https://leetcode.com/contest/weekly-contest-366/problems/minimum-processing-time/


# Solution: We use a greedy algorithm and do the tasks in the order they 
# finish.

# Time complexity: O(nlogn)
# Space complexity: O(1)

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        time_finished = 0
        for i in range(len(processorTime)):
            time_finished = max(time_finished, processorTime[i] + tasks[4*i])
        
        return time_finished