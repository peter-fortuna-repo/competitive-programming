# Problem:
# What is the largest prime factor of the number 600851475143?


 
# Solution
# One simple way to find a number n's prime factorization is by checking all 
# numbers from one to the square root of n. Note that checking for the numbers
# above the square root is unneccesary subce these numbers will be discovered 
# as cofactors to numbers below the square root of n.
#
# To verify if the factors we discover are prime, we keep a record of each
# prime number discovered and check it.
#
# Computational complexity: O(n)
# Explanation: We run through root(n) factors and verify each against up to
#              root(n) possible prime divisors. 
# Storage complexity: O(square root of n)

import math
def solution():
    primes = set()
    max_prime_factor = 1
    factors = []

    n = 600851475143

    def is_prime(num):
        for prime in primes:
            if num % prime == 0:
                return False
        return True

    for i in range(2,int(math.sqrt(n))):
        if is_prime(i):
                primes.add(i)
        if i in primes and n%i == 0:
            max_prime_factor = i
            factors.append(n//i)
    
    for factor in factors:
        if factor > max_prime_factor and is_prime(factor):
            max_prime_factor = factor

    return max_prime_factor