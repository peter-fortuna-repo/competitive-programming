# Link to problem: https://leetcode.com/problems/kth-largest-element-in-an-array

# Solution: 
# This solution uses a similar idea to the quicksort algorithm. Except instead
# of sorting the array, the array is searched for the kth element.

# Time complexity: O(nlogn)
# Space complexityL O(nlogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        pivot = nums[0]
        l, r = [], []

        for num in nums[1:]:
            if num < pivot:
                l.append(num)
            else:
                r.append(num)
            
        if len(r) == k-1:
            return pivot
        elif len(r) >= k:
            return self.findKthLargest(r, k)
        else:
            return self.findKthLargest(l, k - len(r) - 1)