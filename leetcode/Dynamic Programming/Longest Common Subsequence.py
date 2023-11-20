# Link to problem: https://leetcode.com/problems/longest-common-subsequence

# Solution:
# This solution uses memoization to store the longest common subsequence of the 
# current index of text1 and text2. If the current index of text1 and text2 are
# identical, then the longest common subsequence is 1 + the longest common
# subsequence of the next index of text1 and text2. Otherwise, each index is
# incremented and the longest common subsequence is the maximum of the two.

# Time complexity: O(nm)
# Space complexity: O(nm)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[None for _ in range(len(text2))] for _ in range(len(text1))]
        i, j = 0, 0
        return self.helper(text1, text2, i, j, memo)


    def helper(self, text1: str, text2: str, i: int, j: int, memo: List[List[int]]) -> int:
        longest = 0
        if i == len(text1) or j == len(text2):
            return longest
        if memo[i][j] != None:
            return memo[i][j]   

        if text1[i] == text2[j]:
            longest = 1 + self.helper(text1, text2, i+1, j+1, memo)
        else:
            longest = max(self.helper(text1, text2, i+1, j, memo),
                        self.helper(text1, text2, i, j+1, memo))
        memo[i][j] = longest
        return longest