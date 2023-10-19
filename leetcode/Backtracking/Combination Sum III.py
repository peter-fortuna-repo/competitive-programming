# Link to problem: https://leetcode.com/problems/combination-sum-iii


# Solution: 
# This solution uses a depth first search approach. Because the same numbers
# could be searched in different sequences, we can track which combinations of
# digits have already been searched to save some duplicate work.

# Time complexity: O(9^k) 
# Space complexity: O(9^k)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations_searched = set()
        digits_searched = "000000000"
        return self.combinationSum3Helper(k, n, digits_searched, combinations_searched)

    def combinationSum3Helper(self, k, n, digits_searched, combinations_searched):
        if digits_searched in combinations_searched:
            return []
        combinations_searched.add(digits_searched)
        if k < 0 or n < 0:
            return []
        elif k == 0 and n==0:
            return [self.formatDigitsSearched(digits_searched)]

        combinations = []
        for i in range(9):
            if digits_searched[i] == "0":
                next_search = digits_searched[:i] + "1" + digits_searched[i+1:] 
                combinations += self.combinationSum3Helper(k-1, n-(i+1), next_search, combinations_searched)
        
        return combinations

    
    def formatDigitsSearched(self, digits_searched: str) -> List[int]:
        combination = []
        for i in range(9):
            if digits_searched[i] == "1":
                combination.append(i+1)
        
        return combination