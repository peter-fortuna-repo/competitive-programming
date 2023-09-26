# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number
# is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be 
# created from the given combination.


# Solution:
# We place a 1 in the last bit to make this number odd. All of the other 1s go
# to the front of the string to maximize its value. Operations are performed
# with list comprehension instead of using for loops to optimize the algorithm
# a bit.

# Time complexity: O(n) (n = len(s))
# Space complexity: O(n)

def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = sum([c=="1" for c in s])
        return ("".join(["1" for _ in range(num_ones - 1)]) + 
                "".join(["0" for _ in range(len(s) - num_ones)]) + "1")