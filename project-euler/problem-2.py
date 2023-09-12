# Problem:
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.


 
# Solution 1: Bottom up
# Fibonacci numbers are a classic example of dynamic programming, and can be 
# solved using a top down or bottom up method. However, we don't know the 
# number of the "top" term in this problem, which would make this approach 
# messy. A recursive method could also be used, but given the problem goes to 
# Fiboacci numbers in the millions, the O(2^n) runtime is too much.
#
# We find all solutions and only add the even valued terms, which turns out to
# be every third term. This comes from the fact that:
# odd + odd = even
# odd + even = odd
#
# As this sequence adds the two previous terms, it results in the pattern:
# odd, odd, even, odd, odd, even, odd, odd, even, etc
#
# Time complexity: O(n) 
# Space complecity: O(n)

def solution_1():
    fib = dict()
    fib[1] = 1
    fib[2] = 1
    fib[3] = 2
    n = 3
    term = fib[n]
    while term < 4000000:
        term = term + fib[n-1]
        n += 1
        fib[n] = term 

    result = 0
    for i in range(3, n, 3):
           result += fib[i]

    return result



# Solution 2: Bottom up simplified
# We can remove the need for a dictionary by keeping track of the previous term
# and summing even as we come across them.
# 
# Time complexity: O(n)
# Space complexity: O(1)

def solution_2():
    n = 3
    term = 2
    prev = 1
    result = 2

    while term < 4000000:
        temp = term
        term += prev
        prev = temp
        n += 1

        if n%3 == 0:
            result += term 
    
    return result