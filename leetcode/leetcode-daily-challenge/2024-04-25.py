# Link to problem: https://leetcode.com/problems/longest-ideal-subsequence/?envType=daily-question&envId=2024-04-25

# Solution 1: Brute Force
# A solution that considers all possible sequences and returns the longest one.
# The time complexity is exponential and therefore impractical for large 
# inputs.

# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        memo = dict()

        def is_close(c1, c2):
            dif = ord(c1) - ord(c2)
            return dif <= k and dif*-1 <= k

        def helper(c1, s, n):
            if s == "":
                return n
            if len(s) == 1:
                if is_close(c1, s):
                    return n+1
                return n

            query = str((c1, s, n))
            if query in memo.keys():
                return memo[query]

            if is_close(c1, s[0]):
                result = max(helper(s[0], s[1:], n+1), helper(c1, s[1:], n), helper(s[1], s[2:], 0))
                memo[query] = result
            else:
                result = max(helper(c1, s[1:], n), helper(s[0], s[1:], 0))
                memo[query] = result
            return memo[query]

        return helper(s[0], s[1:], 0) + 1


# Solution 2: Dynamic Programming
# A solution that uses dynamic programming to store the maximum length of a
# sequence ending in a given character. The maximum length is calculated by
# adding 1 to the maximum length of the previous characters within the allowed
# distance k.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0] * 26

        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(dp[max(0,i-k):i+k+1]) + 1            
        return max(dp)
