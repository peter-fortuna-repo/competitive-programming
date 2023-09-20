# Problem:
# A Pythagorean triplet is a set of three natural numbers for which a^2+b^2=c^2

# There exists exactly one Pythagorean triplet for which a+b+c=1000.
# Find the product abc.


# Solution 1: Brute Force
# We check all possible natural numbers adding up to the target sum. We check
# each possible value of c and b, computing c as n-(b+c). This gives us a 
# runtime of O(n^2).
#
# Time complexity: O(n^2)
# Space complexity: O(1)

def findTriplet(n = 1000):
    for c in range(n//3+1, n):
        for b in range((n-c)//2, n-c + 1):
            a = n - (b + c)
            if isTriplet(a,b,c):
                return a*b*c
    return -1

def isTriplet(a,b,c):
    return a**2 + b**2 == c**2


# Solution 2: Simplified equation
# There is an additional solution that uses a trick of the math to reduce this
# problem to a(a+b) = n/2, which has a runtime of O(n). As I didn't derive this
# particular equation myself, I won't be coding it up here.
#
# Time complexity: O(n)
# Space complexity: O(1)