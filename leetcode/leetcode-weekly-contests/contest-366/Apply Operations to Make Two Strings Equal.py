# Link to problem: https://leetcode.com/contest/weekly-contest-366/problems/apply-operations-to-make-two-strings-equal/

# Solution: I was unable to complete this problem within the contest's time
# limit. However, an incomplete dynamic programming solution is written below.
# The recursive step does not consider all possible flips (line 37) and 
# therefore does not work for all cases.

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        dif = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                dif += 1
        if dif % 2 != 0:
            return -1
        
        if x == 1:
            return dif // 2
        
        memo = dict()
        return self.minOperationsHelper(s1, s2, x, n-1, memo)
    
    def minOperationsHelper(self, s1: str, s2: str, x: int, n: int, memo: dict) -> int:
        if s1 == s2:
            return 0
        while s1[n] == s2[n]:
            n -= 1
        if s1[:n] in memo:
            return memo[s1[:n]]
        m = n - 1
        while s1[m] == s2[m]:
            m -= 1
        memo[s1[:n]] = min(1 + self.minOperationsHelper(self.flipBits(s1, n-1, n), s2, x, n-1, memo), 
                            x + self.minOperationsHelper(self.flipBits(s1, m, n), s2, x, m-1, memo))
        return memo[s1[:n]]
                
                            
    def flipBits(self, s1: str, i: int, j: int) -> str:
        new_bit1 = "0"
        new_bit2 = "0"
        if s1[i] == "0":
            new_bit1 = "1"
        if s1[j] == "0":
            new_bit2 = "1"
        return s1[:i] + new_bit1 + s1[i+1:j] + new_bit2 + s1[j+1:]