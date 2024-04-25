# Link to problem: https://leetcode.com/problems/n-th-tribonacci-number/submissions/1240799703/?envType=daily-question&envId=2024-04-24

# Solution 1: Bottom Up
# The nth tribonocci number is found by first findin all n-l that come before 
# it. To save space, only the last 3 numbers are stored.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        prev_1 = 0
        prev_2 = 1
        cur = 1

        for _ in range(n-2):
            temp = cur

            cur = prev_1 + prev_2 + cur
            prev_1 = prev_2
            prev_2 = temp
    
        return cur
    
    
    
# Solution 2: Top Down
# This solution uses a cache to track the nth tribonocci number. If the number
# is already in the cache, it is returned. Otherwise, the number is calculated
# recursively and stored in the cache.

# Time complexity: O(n)
# Space complexity: O(n)


class Solution(object):
    memo = dict()
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo.keys():
            return self.memo[n]
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]