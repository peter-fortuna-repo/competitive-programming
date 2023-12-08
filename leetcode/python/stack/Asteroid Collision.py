# Problem:
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign 
# represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids 
# meet, the smaller one will explode. If both are the same size, both will 
# explode. Two asteroids moving in the same direction will never meet.

# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.



# Solution: 
# We add each asteroid to a stack, then check for collisions. If the asteroid 
# collides, we check the relative sizes and pop the smaller asteroid.

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            result.append(asteroid)
            self.checkCollisions(result)
        return result

    def checkCollisions(self, result):
        if len(result) < 2:return
        if result[-2] * result[-1] > 0: return
        if result[-2] < 0: return 

        # Collision detected 
        if abs(result[-2]) == abs(result[-1]):
            result.pop()
            result.pop()
        elif abs(result[-2]) > abs(result[-1]):
            result.pop()
        else:
            result.pop(-2)
        self.checkCollisions(result)
        return