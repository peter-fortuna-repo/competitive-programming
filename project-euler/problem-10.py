# Problem:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

# Find the sum of all the primes below two million.


# Solution:
# Another prime number problem. We use the same prime finding algorithm which
# involves storing all known primes and checking against the primes less than
# a number's square root.

# Time complexity: O(n^2)
# Space complexity: O(n)

def solution(n=2000000):
    primes = [2]
    sum = 2
    for i in range(3,n):
        if isPrime(i, primes):
            primes.append(i)
            sum += i 
    return sum


def isPrime(n, primes):
    for prime in primes:
        if prime * prime > n:
            return True
        if n%prime == 0:
            return False
        

if __name__ == "__main__":
    print(solution())