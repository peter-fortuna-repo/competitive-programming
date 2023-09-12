# Problem:
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


# Solution:
# This solution is straightforward. It uses few operations and is made more 
# efficient by using list comprehension.
#
# Time complexity: O(n)
# Space complexity: O(n)

def solution(n=100):
    return sum([i for i in range(1,n+1)])**2 - sum([i**2 for i in range(1,n+1)])