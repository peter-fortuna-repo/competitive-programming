# Link to problem: https://leetcode.com/problems/total-cost-to-hire-k-workers

# Solution 1:
# This solution keeps a heap for the left and right sides of the array. In each
# iteration, the lowest cost candidate is removed and the heaps are updated 
# with the next avaliable element from costs. When costs is empty, they are 
# updated with a value larger than the maximum input.

# Time complexity: O(n)
# Space complexity: O(n)

from heapq import heapify, heappush, heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) == 1:
            return costs[0]

        l = min(candidates, len(costs)//2)
        r = -min(candidates, len(costs)//2)
        left_heap = costs[:l]
        right_heap = costs[r:]
        heapify(left_heap)
        heapify(right_heap)

        left_min = heappop(left_heap)
        right_min = heappop(right_heap)

        total_cost = 0
        num_workers = 0
        while num_workers < k:
            min_cost = min(left_min, right_min)
            if left_min <= right_min:
                if l - r < len(costs):
                    heappush(left_heap, costs[l])
                    l += 1
                if left_heap:
                    left_min = heappop(left_heap)
                else:
                    left_min = 10**6

            else:
                if l - r < len(costs):
                    r -= 1
                    heappush(right_heap, costs[r])
                if right_heap:
                    right_min = heappop(right_heap)
                else:
                    right_min = 10**6    
            total_cost += min_cost
            num_workers += 1

        return total_cost


# Solution 2: Denser and slightly less efficient

# Here, I implemented an identicle solution but made it more readable. Several
# if statements have been reduced to one line statements and other aspects of
# the solution have been streamlined. The costs array is modified as well, 
# which is not necessary but aids in making the code readable.

# Time complexity: O(n)
# Space complexity: O(n)

from heapq import heapify, heappush, heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap, right_heap = [], []
        heapify(left_heap)
        heapify(right_heap)

        total_cost = 0
        for _ in range(k):
            while len(left_heap) < candidates:
                heappush(left_heap, costs.pop(0) if costs else 10**6)
            while len(right_heap) < candidates:
                heappush(right_heap, costs.pop() if costs else 10**6)

            total_cost += heappop(left_heap) if left_heap[0] <= right_heap[0] else heappop(right_heap) 

        return total_cost