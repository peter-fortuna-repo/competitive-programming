# Link to problem: https://leetcode.com/problems/maximum-subsequence-score

# Solution:
# This solution starts by sorting both arrays in the decreasing order of nums2.
# A heap is used to keep track of the largest elements in nums1, so that 
# prefix_sum is always at the maximum value given the a mimum nums2.

# Time complexity: O(nlog(n))
# Space complexity: O(n)

from heapq import heapify, heappop, heappush

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:        
        # Joint sorting
        combined = list(zip(nums2, nums1))
        combined.sort(reverse = True)
        nums1 = [value[1] for value in combined]
        nums2 = [value[0] for value in combined]

        prefix_sum, nums1_heap, max_score = 0, [], 0
        heapify(nums1_heap)

        for i in range(len(nums2)):
            nums2_min = nums2[i]         
            heappush(nums1_heap, nums1[i])
            prefix_sum += nums1[i]
            if len(nums1_heap) == k:
                max_score = max(max_score, nums2_min * prefix_sum)
                prefix_sum -= heappop(nums1_heap)

        return max_score