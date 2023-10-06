# Link to problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

# Solution:
# The brute force approach would involve counting all vowels in the window of 
# size k. Instead, we can use two pointers and keep a running tally of the 
# vowel count. This saves us computation and brings the process down to O(n).

# Time complexity: O(n) 
# Space complexity: O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        i = 0
        j = k
        count = 0
        for c in s[:j]:
            if c in vowels:
                count += 1
        
        max_count = count
        while j < len(s):
            if s[i] in vowels:
                count -= 1
            if s[j] in vowels:
                count += 1
            max_count = max(count, max_count)
            i += 1
            j += 1

        return max_count