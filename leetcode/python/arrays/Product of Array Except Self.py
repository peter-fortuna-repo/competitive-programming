# Given an integer array nums, return an array answer such that answer[i] is 
# equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.

# You must write an algorithm that runs in O(n) time and without using the 
# division operation

# Solution 1: Brute Force
# The simplest approach is to loop through every element in the array and 
# find the required products. However, this is O(n^2), and the algorithm needs
# to be O(n)

# Time complexity: O(n^2) 
# Space complexity: O(n)

def productExceptSelf(nums: List[int]) -> List[int]:
    products = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in (x for x in range(len(nums)) if x != i):
            products[i] *= nums[j]
    
    return products


# Solution 2: Store partial products
# We can save duplicate work by storing partial products. If division were 
# allowed, we could store the product of the entire array and divide by 
# nums[i]. However, the problem definition forbids this, so we need another 
# approach. Instead, we can make an array of "left products" and an array of
# "right products", where the left products is the product of all elements left
# of i and right products is the reverse. Then, to find the product for i, we 
# multiply the left and the right products together. As each step here takes 
# one sweep through the nums array, the final runtime is O(n).

# Time complexity: O(n)
# Space complexity: O(n)

def productExceptSelf(nums: List[int]) -> List[int]:
    left_products = [None] * len(nums)
    right_products = [None] * len(nums)
    
    left_products[0] = nums[0]
    for i in range(1,len(nums)-1):
        left_products[i] = left_products[i-1] * nums[i]
    
    right_products[-1] = nums[-1]
    for i in range(len(nums)-2, 0, -1):
        right_products[i] = right_products[i+1] * nums[i]

    final_products = [None] * len(nums)
    final_products[0] = right_products[1]
    final_products[-1] = left_products[-2]
    for i in range(1,len(nums)-1):
        final_products[i] = left_products[i-1] * right_products[i+1]
    return final_products