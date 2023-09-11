# Given an integer n, return an array ans of length n + 1 such that for each i 
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# Solution 1: Bit shift solution
# We simply go through all numbers 0 to n and count the number of bits in the 
# binary representaiton. As each int has log(n) bits, the count_binary function
# runs in O(logn) time, and the entire algorithm runs in O(nlogn) time.

# Time complexity: O(nlogn)
# Space complexity: O(n)

def countBits(self, n: int) -> List[int]:
    ans = [None] * (n+1)
    
    def count_binary(i):
        count = 0
        for offset in range(20):
            if (i & 1<<offset) != 0:
                count += 1
        return count

    for i in range(n+1):
        ans[i] = count_binary(i)
    
    return ans

# Solution 2: Dynamic solution
# We can make our algorithm more efficient using a recurrence relation. Note 
# that for some power of two (p), the binary represenation contains a single bit.
# Note also that each number from p to 2p will have the same binary 
# represenation as the numbers from 0 to p, with a single extra bit in the most
# signfigant position. IE:
#    0 = 00000          16 = 10000
#    1 = 00001          17 = 10001
#    2 = 00010          18 = 10010
#    3 = 00011          19 = 10011
# etc. 
# Using, this recurrence relation, we can refer to the number of bits in
# position i-p to quickly find the number of bits in i.

# Time complexity: O(n)
# Space complexity: O(n)

def countBits(self, n: int) -> List[int]:
    ans = [0] * (n+1)
    if n == 0:
        return ans
        
    ans[1] = 1
    power = 1
    for i in range(2,n+1):
        if i % power == 0:
            power *= 2
            ans[i] = 1
        else:
            ans[i] = ans[i - power] + 1
    
    return ans