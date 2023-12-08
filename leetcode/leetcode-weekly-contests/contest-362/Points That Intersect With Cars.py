# Link to problem: https://leetcode.com/contest/weekly-contest-362/problems/points-that-intersect-with-cars/

# Solution 1: Brute force 
# This solution creates an array for the number line and sets it to True if
# covered by a car. As the same spots can be repeatedly set to True multiple
# times - n times in the worst case - this solution isn't optimal.

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        number_line = [False] * 101  # To avoid adjusting from 0 indexed to 1 indexed
        for num in nums:
            number_line[num[0]:num[1]+1] = [True] * (1 + num[1] - num[0])
        
        return sum(number_line)

# Solution 2: Sorted Search
# This approach saves time resetting the array to true by first sorting the 
# list of nums. In this solution, each index of number_line is set to true at
# most one time.

# Time complexity: O(nlogn)
# Space comlexity: O(n)

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:        
        number_line = [False] * 100
        nums.sort()
        number_line[nums[0][0]:nums[0][1]+1] = [True] * (1 + nums[0][1] - nums[0][0])
        max_index = nums[0][1]
        for i in range(1,len(nums)):
            if nums[i][1] <= max_index:
                continue
            elif nums[i-1][1] > nums[i][0]:
                number_line[nums[i-1][1]:nums[i][1]+1] = [True] * (1 + nums[i][1] - nums[i-1][1])
            else:
                number_line[nums[i][0]:nums[i][1]+1] = [True] * (1 + nums[i][1] - nums[i][0])
            max_index = max(max_index, nums[i][1])
        return sum(number_line)