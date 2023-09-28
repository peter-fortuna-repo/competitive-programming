# You have a long flowerbed in which some of the plots are planted, and some 
# are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be 
# planted in the flowerbed without violating the no-adjacent-flowers rule and 
# false otherwise.

 


# Solution:
# A greedy solution works here. As any solution will need to scan through all 
# elements in flowerbed, the big O for the runtime for of this algorithm cannot
# be improved. 

# To cleanly manage indexing issues for -1 and n+1, I appended a 0 to 
# flowerbed. This makes it so flowerbed[-1] = 0 and flowerbed[n+1] = 0, which 
# is the appropriate value for this problem.

# Time complexity: O(n)
# Space complexity: O(1)


def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    # Edge cases
    if n == 0:
        return True
    if len(flowerbed) == 1:
        return n==1 and flowerbed[0] == 0

    # Algorithm
    l = len(flowerbed)
    flowerbed.append(0)
    num_planted = 0
    for i in range(l):
        prev = flowerbed[i-1]
        cur = flowerbed[i] 
        nxt = flowerbed[i+1]

        if prev + cur + nxt == 0: 
            flowerbed[i] = 1
            num_planted += 1

    return num_planted >= n