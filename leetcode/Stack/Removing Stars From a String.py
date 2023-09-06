# You are given a string s, which contains stars *.
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
#
# Return the string after all stars have been removed.

# Solution 1:
# This problem is simple using a stack. Append letters and pop() for each star.

# Computational complexity: O(n) 
# Space complexity: O(n)

def removeStars(self, s: str) -> str:
        answer = []
        for c in s:
            if c == "*":
                answer.pop()
            else:
                answer.append(c)
        
        return "".join(answer)

# Solution 2:
# For an added challenge we solve the problem in place. To do so, we first 
# count the number of stars and remove parts of the string until all stars have
# been removed.

def removeStars(self, s: str) -> str:
        num_stars = 0
        for c in s:
            if c == "*":
                num_stars += 1

        i = 0
        while num_stars > 0:
            i += 1
            if s[i] == "*":
                j = i-1
                while i < len(s)-1 and s[i+1] == "*":
                    i += 1
                    j -= 1
                s = s[:j] + s[i+1:]
                num_stars -= (1+i-j)/2
                i = j

        return s

# Computational complexity: O(n)
# Space complexity: O(1)