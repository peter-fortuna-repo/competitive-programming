# Link to Problem: https://leetcode.com/problems/domino-and-tromino-tiling

# Solution: Bottom up
# We start with the base cases and build up to the final answer. Every tile 
# from n-1 can have a verical domino placed next to it. Every tile from n-2 can
# have two horizontal dominos placed next to it. All the previous tiles from 
# n-3 to 0 can have a distinct sequence of trominos placed next to it, and this 
# sequence can be flipped, so we multiply by 2. We add all these possibilities 
# to get the next tile. Modulo is used to keep the numbers small and avoid 
# overflow.

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def numTilings(self, n: int) -> int:
        tilings = [1,1,2,5]
        mod = 1000000007
        while len(tilings) < n+1:
            next_tile = tilings[-1]
            next_tile += tilings[-2]
            next_tile += sum([tilings[-i]*2 for i in range(3,len(tilings)+1)])
            tilings.append(next_tile % mod)
        return tilings[n]