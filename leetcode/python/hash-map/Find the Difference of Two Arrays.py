# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of 
# size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

# Solution: 
# This problem is relatively straightforward. The main trick is to convert each
# list of numbers to a set for quick lookup, then check each number.

# Time complexity: O(n) 
# Space complexityL O(n)

def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    distinct1 = set()
    set2 = set(nums2)
    distinct2 = set()

    for num in nums1:
        if num not in set2:
            distinct1.add(num)

    for num in nums2:
        if num not in set1:
            distinct2.add(num)

    return [list(distinct1), list(distinct2)]