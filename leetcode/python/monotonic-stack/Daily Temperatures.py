# LInk to problem: https://leetcode.com/problems/daily-temperatures/submissions


# Solution 1: Right to left
# This approach moves through the temperature array from the right to left and
# tracks the indecices of the largest temperatures in order. The hottest 
# temperature will always be on the bottom of the stack, then the second
# hottest that has a smaller index will be on top of that and so on. At each
# index, this stack is used to determine the value of index i and updated.

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack and temperatures[stack[-1]] > temperatures[i]:
                answer[i] = stack[-1] - i
            stack.append(i)

        return answer

# Soltuion 2: Left to right
# This approach moves from left to right and may be more intuitive. For each
# index in the answer array, the answer is updated the first time a higher
# temperature is found.

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                current = stack.pop()
                answer[current] = i - current
            stack.append(i)

        return answer