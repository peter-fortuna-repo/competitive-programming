# Link to problem: https://leetcode.com/problems/successful-pairs-of-spells-and-potions


# Solution: 
# This approach starts by sorting potions. This lets you apply a binary search
# algorithm on potions to find the smallest viable potion for each spell. Once 
# you know this, you can quickly calculate the number of pairs.

# Time complexity: O(nlog(m)) 
# Space complexity: O(1)


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []

        for spell in spells:
            i = self.smallestPair(spell, potions, success)
            pairs.append(len(potions) - i)
        return pairs

    def smallestPair(self, spell, potions, success):
        i = len(potions) // 2
        low = 0
        high = len(potions)
        while i > 0:
            i = (high + low) // 2
            if potions[i] * spell >= success:
                if potions[i-1] * spell < success:
                    return i
                high = i
            else:
                low = i
                if i == len(potions)-1:
                    return i+1
        return i