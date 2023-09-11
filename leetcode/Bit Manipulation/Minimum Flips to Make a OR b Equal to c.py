# Given 3 positives numbers a, b and c. Return the minimum flips required in 
# some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 
# to 1 in their binary representation.


# Solution:
# To solve this problem, we start by creating a simple bit operation function 
# that checks whether a bit at position i from the right is 0 or 1. We then 
# move through ints c, b, and a from their rightmost bit (least signifigant bit) 
# to  their leftmost (most signifigant) bit. If bits must be changed, "flips" 
# is incremented and finally returned.

# Time complexity: O(n)
# Space complexity: O(1)

def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        def get_bit(num, i):
            return num & (1 << i) != 0

        for i in range(32):
            if get_bit(c, i) and not get_bit(a,i) and not get_bit(b,i):
                flips += 1
    
            elif not get_bit(c,i):
                if get_bit(a,i):
                    flips += 1
                if get_bit(b,i):
                    flips += 1

return flips