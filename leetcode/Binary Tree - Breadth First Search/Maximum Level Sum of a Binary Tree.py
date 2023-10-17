# Link to problem: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Solution: 
# We can perform a breadth first search and sum the value of the elements in
# each row. This takes O(n) time and  space equal to the two largest row, which
# is at most O(n).

# Time complexity: O(n)  
# Space complexity: O(n) 

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -inf
        max_sum_level = 1

        level = 1
        next_level_nodes = []
        current_level_nodes = [root]

        while current_level_nodes:
            row_sum = 0
            for node in current_level_nodes:
                row_sum += node.val
                if node.left != None:
                    next_level_nodes.append(node.left)
                if node.right != None:
                    next_level_nodes.append(node.right)
            if row_sum > max_sum:
                max_sum_level = level
                max_sum = row_sum

            level += 1
            current_level_nodes = next_level_nodes
            next_level_nodes = []

        return max_sum_level