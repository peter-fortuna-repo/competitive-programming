# Problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
# 3, 5, 6, and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.


 
# Solution 1:
# Loop through all multiples of 3 and 5 and add them together, then subtract all 
# multiples of 15 because they get double counted.

# Time complexity: O(n) (where n is the upper limit, ie 1000)
# Space complexity: O(1)

def solution_1():
        sum = 0

        # Add multiples of 3
        for i in range(0,1000,3):
            sum += i

        # Add multiples of 5
        for i in range(0,1000,5):
            sum += i

        # Remove duplicate multiples of 15
        for i in range(0,1000,15):
            sum -= i

        return sum


# Solution 2
# We can speed this up using a math trick.
# Note that:
# 3(0) + 3(1) + 3(2) + ... + 3(332) + 3(333)
# 
# Simplifies to:
# 3(1 + ... + 332 + 333)
# 
# Because the sum from one to n is n(n+1)/2, we get:
# 3 (333 * 334 / 2)
# 
# This allows us to solve the problem in constant time.

# Time complexity: O(1)
# Space complexity: O(1)

def solution_2():
        def sumMultiples(m, n):
              return m*(n//m)*(n//m+1)//2 # As explained above
        
        return sumMultiples(3,1000) + sumMultiples(5,1000) - sumMultiples(15,1000)