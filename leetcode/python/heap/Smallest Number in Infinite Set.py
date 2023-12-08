# Link to problem: https://leetcode.com/problems/smallest-number-in-infinite-set

# Solution: Hard coded limit
# This solution tracks whether an element has been added or removed using a
# boolean array and returns the smallest element. This solution works 
# effeciently given the upper limit of 1000 function calls. However, it does 
# not scale.

# Time complexity: O(n)
# Space complexity: O(n)

class SmallestInfiniteSet:
    def __init__(self):
        self.firstThousand = [True] * 1000

    def popSmallest(self) -> int:
        for i in range(1000):
            if self.firstThousand[i]:
                self.firstThousand[i] = False
                return i+1

    def addBack(self, num: int) -> None:
        self.firstThousand[num-1] = True


# Solution: True solution

# This solution uses a simlilar technique but it scales.

# Time complexity: O(n)
# Space complexity: O(n)

class SmallestInfiniteSet:
    def __init__(self):
        self.largest_removed = 0
        self.nums_added = set()

    def popSmallest(self) -> int:
        if self.nums_added:
            smallest = min(self.nums_added)
            self.nums_added.remove(smallest)
            return smallest
        else:
            self.largest_removed += 1
            return self.largest_removed

    def addBack(self, num: int) -> None:    
        if num <= self.largest_removed:
            self.nums_added.add(num)