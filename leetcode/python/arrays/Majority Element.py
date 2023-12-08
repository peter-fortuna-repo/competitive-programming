# Link to problem: https://leetcode.com/problems/majority-element

# Solution 1: Dictionary
# This solution uses a dictionary to keep track of the number of times each 
# number appears in nums. Once a number appears more than len(nums)/2 times, it
# is returned.

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 0
            num_counts[num] += 1
            if num_counts[num] > len(nums)/2:
                return num

# Solution 2: Stack
# This solution uses a stack to keep track of the majority element. The first
# number is added to the stack. If the next number is the same as the top of 
# the stack, it is added to the stack. If it is different, the top of the stack
# is removed. The majority element will always be the last element in the stack

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:    
    def majorityElement(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack or num == stack[-1]:
                stack.append(num)
            else:
                stack.pop()
        return stack.pop()

# Solution 3: O(1) space
# This solution is the same as solution 2, but uses O(1) by maintaining a count
# of the stack size instead of maintaining the stack itself.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num = -1
        count = 0
        for num in nums:
            if count == 0 or num == majority_num:
                majority_num = num
                count += 1
            else:
                count -= 1
        return majority_num