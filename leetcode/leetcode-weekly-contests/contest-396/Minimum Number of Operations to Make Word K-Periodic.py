# Link to problem: https://leetcode.com/problems/valid-word/description/

# Solution
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        digits = {'0','1','2','3','4','5','6','7','8','9'}
        vowels = {'a','e','i','o','u'}
        consonants = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
        if len(word) < 3:
            return False
        hasVowel = False
        hasConsonant = False
        for c in word:        
            c = c.lower()
            if c in consonants:
                hasConsonant = True
            elif c in vowels:
                hasVowel = True
            elif c not in digits:
                return False

        if hasVowel and hasConsonant:
            return True
        return False