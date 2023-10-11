# Link to problem: https://leetcode.com/contest/weekly-contest-366/problems/divisible-and-non-divisible-sums-difference/

# Solution: This problem is relatively straightforward. We can solve if by
# checking all numbers 1 to n for divisibility by m and computing the requested
# sum.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = 0
        nums2 = 0
        for i in range(1,n+1):
            if i % m != 0:
                nums1 += i
            else:
                nums2 += i
        
        return  nums1 - nums2