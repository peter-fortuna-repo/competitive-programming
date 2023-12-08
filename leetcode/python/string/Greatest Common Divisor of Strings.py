# For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.

# Solution:
# It's straightforward enough to find the shortest substring divisor. To find
# the longest divisor, we count the number of times this shortest divisor is 
# repeated in each string and get the greatest common denominator between these
# two numbers. Multiply the shortest divisor by the GCD and we have our longest
# divisor.

# Time complexity: O(n)
# Space complexity: O(1)

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        str1_pattern = self.getShortestRepeat(str1,1)
        str2_pattern = self.getShortestRepeat(str2,1)
        if str1_pattern != str2_pattern:
            return ""
        repeats1 = len(str1.split(str1_pattern)) - 1
        repeats2 = len(str2.split(str2_pattern)) - 1
        gcd = math.gcd(repeats1, repeats2)
        return str1_pattern * gcd

    def getShortestRepeat(self, s: str, i: int) -> str:
        if len(s) < 2*i:
            return s
        if s[0:i] == s[i:i*2] and self.isDivisible(s, s[0:i]):
            return s[0:i]
        return self.getShortestRepeat(s, i+1)

    def isDivisible(self, s: str, pattern: str) -> bool:
        if "".join(s.split(pattern)) == "":
            return True
        return False
