# There are n kids with candies. You are given an integer array candies, where 
# each candies[i] represents the number of candies the ith kid has, and an 
# integer extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if, after 
# giving the ith kid all the extraCandies, they will have the greatest number 
# of candies among all the kids, or false otherwise.


# Solution 1: 
# The best possible algorithm is O(n) in time and space, as we must check all 
# indexes and return an array of length n. We can use list comprehension to 
# speed things up slightly.

# Time complexity: O(n) 
# Space complexity: O(n)

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]