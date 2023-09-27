# Given an array of integers arr, return true if the number of occurrences of 
# each value in the array is unique or false otherwise.

# Solution: 
# This problem is relatively straightforward. First, we make a dictionary
# counting the number of occurrences of each element in arr. Then, we check 
# that each elemnt is indeed unique by inserting it into a set.

# Time complexity: O(n) 
# Space complexityL O(n)

def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        for num in arr:
            if not num in counts:
                counts[num] = 0
            counts[num] += 1
        distinct_counts = set()
        for count in counts.values():
            if count in distinct_counts:
                return False
            distinct_counts.add(count)
        return True