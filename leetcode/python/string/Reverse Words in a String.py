# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will 
# be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Solution: Python Standard Library
# The simplest approach is to use built in Python methods for this

# Time complexity: O(n) 
# Space complexity: O(n)

def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
