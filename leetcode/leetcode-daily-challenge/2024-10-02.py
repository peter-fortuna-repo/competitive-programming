# Solution
# Space complexity: O(n)
# Computational complexity: O(nlogn)

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set = set(arr)
        sorted_arr = sorted(arr_set)
        rank_map = dict()

        for i, val in enumerate(sorted_arr):
            rank_map[val] = i+1
        ranks = []
        for val in arr:
            ranks.append(rank_map[val])
        
        return ranks