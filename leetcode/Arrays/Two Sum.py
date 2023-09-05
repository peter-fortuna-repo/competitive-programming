# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution 1: 
# The simplest approach is to check all possible pairs in a nested loop 

# Computational complexity: O(n^2) 

def twoSum(nums, target):
    for i in range(nums.size-1):
        for j in range(i+1, nums.size)
            if nums[i] + nums[j] == target:
                return (i, j)
            
    return None


# Solution 2
# We can bring the runtime down to O(n). When we check nums[i], we know that
# the other element must equal target - nums[i]. This lets us speed things up 
# using a hashtable. After a hashtable linking nums[i] to i is built,  we pass 
# through nums one time, and at each num we check if the needed element is in 
# our hashtable.

# Computational complexity: O(n)

def twoSum(nums, target):
    lookup = {}
    for i in range(nums.size):
        lookup.add(nums[i], i)

    for i in range (nums.size):
        lookup.remove(nums[i], i)
        if lookup[target - nums[i]]:
            return (i, lookup.get(target - nums[i]))
        
        lookup.add(nums[i], i)

    return None