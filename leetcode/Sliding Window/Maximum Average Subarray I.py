# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum 
# average value and return this value.

# Solution 1: Brute Force
# Use a sliding window to check all possible averages

# Computational complexity: O(kn) 

def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_avg = -10000 # Smallest possible input
    for i in range(len(nums)-k+1):
        avg = sum(nums[i:k+i])/k
        if avg > max_avg:
            max_avg = avg
    return max_avg
        

# Solution 2: 
# Use a sliding window and a running sum to avoid repeatedly summing i+1 through 
# k-1. This way, only two elements are needed to calculate each average.

# Computational complexity: O(n)

def findMaxAverage(self, nums: List[int], k: int) -> float:
    total = sum(nums[0:k])
    max_avg = total/k
    for i in range(1, len(nums)-k+1):
        total -= nums[i-1]
        total += nums[k+i-1]
        avg = total/k
        if avg > max_avg:
            max_avg = avg
    return max_avg