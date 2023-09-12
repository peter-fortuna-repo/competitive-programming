# Problem:
# Find the 10,001st prime number.


# Solution:
# To find the 10,001st prime, we find each prime from the first to the 
# 10,000th, and check each integer for divisibility by this set of prime 
# numbers.
#
# Time complexity: O(n^2)
# Space complexity: O(n)

def solution(n=10001):
    primes = [2]
    i = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1
    return primes[-1]