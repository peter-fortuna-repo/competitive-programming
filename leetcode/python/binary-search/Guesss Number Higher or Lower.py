# Problem:
# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is 
# higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).

# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6


# Solution: 
# The simplest approach would be to check all numbers from 1 to n. However, 
# this will take O(n) guesses and is inefficient. Instead, we can do a binary 
# search in O(log(n)) time.

# Time complexity: O(log(n)) 
# Space complexity: O(1)


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        return self.guessNumberHelper(0,n)

    def guessNumberHelper(self, n_lower:int, n_upper:int) -> int:
        n_mid = n_lower + (1 + n_upper - n_lower)//2
        result = guess(n_mid) # API provided by LeetCode -- explained above
        if result == -1:
            return self.guessNumberHelper(n_lower, n_mid)
        elif result == 1:
            return self.guessNumberHelper(n_mid, n_upper)
        else:
            return n_mid