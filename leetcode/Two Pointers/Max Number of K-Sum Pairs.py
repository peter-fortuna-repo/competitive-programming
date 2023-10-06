# Link to problem: https://leetcode.com/problems/max-number-of-k-sum-pairs

# Solution: 
# To solve this problem, I created a hash map that counts the number of 
# occurences of each int. Then I loop through the hashmap and instantly know
# what the complement (target - number) of each number is and can look for it
# in the hashmap. 

# Time complexity: O(n)
# Space complexity: O(n)
 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operation_count = 0
        num_counts = dict()
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 0
            num_counts[num] += 1
        
        for num in nums:
            compliment = k - num
            if compliment == num and num_counts[num] < 2:
                continue
            if (compliment in num_counts and num_counts[compliment] > 0
                and num_counts[num] > 0):
                operation_count += 1
                num_counts[compliment] -= 1
                num_counts[num] -= 1

        
        return operation_count