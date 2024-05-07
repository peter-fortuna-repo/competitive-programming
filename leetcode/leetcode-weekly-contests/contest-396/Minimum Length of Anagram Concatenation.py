# Link to problem: https://leetcode.com/problems/minimum-length-of-anagram-concatenation/description/

# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for k in range(1,n//2 + 1):
            if n % k != 0:
                continue

            anagram_letters = [0] * 26
            for c in s[:k]:
                anagram_letters[ord(c) - ord('a')] += 1
            
            i = 1
            validAnagram = True
            while validAnagram and i != n/k:
                next_k_letters = [0] * 26
                for c in s[k*i: k*(i+1)]:
                    next_k_letters[ord(c) - ord('a')] += 1
                if next_k_letters != anagram_letters:
                    validAnagram = False 
                i += 1
            
            if validAnagram:
                return k
        return n