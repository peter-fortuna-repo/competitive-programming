# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.

# Solution: 
# First, the string is converted to a list so that it becomes mutable. Each 
# vowel is added to a stack, then inserted into the appropriate spot.

# Time complexity: O(n) 
# Space complexity: O(n)

def reverseVowels(self, s: str) -> str:
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    vowel_stack = []
    indexes = []

    s = list(s)
    for i, c in enumerate(s):
        if c in vowels:
            vowel_stack.append(c)
            indexes.append(i)
    
    for i in indexes:
        s[i] = vowel_stack.pop()
    return "".join(s)