# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

# Solution: 
# This problem is straightforward to solve using recursion. 

# Time complexity: O(n)  
# Space complexity: O(n)

def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1