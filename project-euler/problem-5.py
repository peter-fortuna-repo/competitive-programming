# Problem:
# What is the smallest positive number that is divisible by all of the numbers 
# from 1 to 20?


# Solution:
# Consider the prime factorization of all numbers between 1 and n. We want to
# find a number X with a prime factorization such that any of the prime 
# factorizations between 1 and n is a subset of X's factorization. If we
# multiply the highest power of each prime between 1 and n, this will give us
# the target number. 
#
# To find the necessary primes and powers of primes, we go from 1 o n,
# tracking all primes and checking for divisibility.
#
# Time complexity: O(n^2) 
# Space complexity: O(n)

def solution():
    n = 20
    primes = set()
    max_powers = set() # Our solution uses the max power of each prime. Ie 16=2^4

    def find_prime_factor(num):
        for prime in primes:
            if num%prime == 0: return prime
        return 0

    def is_power_of(num, prime):
        quotient = num/prime
        while float(quotient).is_integer():
            quotient = quotient/prime
            if quotient == 1:
                return True
        return False

    for i in range(2,n):
        factor = find_prime_factor(i)
        if factor and is_power_of(i, factor):
            max_powers.remove(i/factor) # prime_factor^n-1
            max_powers.add(i)
        
        if factor == 0:
            primes.add(i)
            max_powers.add(i)
    
    product = 1
    for factor in max_powers:
        product *= factor

    return product