# Problem:
# Find the largest palindrome made from the product of two 3-digit numbers.


# Solution:
# We loop through all possible products of 3-digit numbers. Our inner loop
# is constrained to avoid double checking products (ie 100*999 and 999*100).
#
# Computational complexity: O(n^2) 
# Storage complexity: O(1)

def solution():
    def is_palindrome(num):
        n = len(str(num))//2
        if str(num)[:n] == str(num)[-1:-n-1:-1]:
            return True
        return False 
    
    max_palindrome = -1
    for i in range(100, 1000):
        for j in range(100, i):
            product = i * j
            if product > max_palindrome and is_palindrome(product):
                max_palindrome = product 
    
    return max_palindrome