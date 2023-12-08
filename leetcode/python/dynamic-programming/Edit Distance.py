# Link to problem: https://leetcode.com/problems/edit-distance/

# Solution:
# This solution use memoization to find the minimum edit distance. It is based
# on the idea that each letter in word1 is either a match, is changed, added, 
# or removed. This recursive solution checks every possible operation and 
# returns the solution that results in the least number of operations.

# Time complexity: O(n + m) 
# Space complexity: O(nm)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        memo[" "] = 0
        return self.helper(word1, word2, memo)

    def helper(self, word1: str, word2: str, memo: dict) -> int:
        key = word1 + " " + word2
        if key in memo:
            return memo[key]
        if word1 == "":
            memo[key] = len(word2)
        elif word2 == "":
            memo[key] = len(word1)
        elif word1[0] == word2[0]:
            memo[key] = self.helper(word1[1:], word2[1:], memo)
        else:
            memo[key] = 1 + min(self.helper(word1[1:], word2, memo),
                            self.helper(word1, word2[1:], memo),
                            self.helper(word1[1:], word2[1:], memo))
        return memo[key]