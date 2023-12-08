# Link to problem: https://leetcode.com/problems/string-compression

# Solution: 
# This problem can be solved in one pass through chars using two pointers. The
# second pointer moves through the entire array, while the first pointer keeps 
# track of the position to update.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        p1 = 0
        p2 = 1
        c = chars[0]
        count = 1
        while p2 < len(chars):
            if chars[p2] == c:
                count += 1

            if c != chars[p2]:
                chars[p1] = c
                p1 += 1
                if count > 1:
                    for digit in str(count):
                        chars[p1] = digit
                        p1 += 1
                c = chars[p2]
                count = 1
            p2 += 1   
        

        chars[p1] = c
        p1 += 1

        if count > 1:
            for digit in str(count):
                        chars[p1] = digit
                        p1 += 1

        return p1