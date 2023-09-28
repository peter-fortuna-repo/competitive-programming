# Consider all the leaves of a binary tree, from left to right order, the 
# values of those leaves form a leaf value sequence.

# Two binary trees are considered leaf-similar if their leaf value sequence is 
# the same.

# Return true if and only if the two given trees with head nodes root1 and 
# root2 are leaf-similar.

# Solution: 
# This simple recursive method will return the desired sequence. It goes 
# through each node one time, so it has O(n) time complexity.

# Time complexity: O(n) 
# Space complexity: O(1)

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leafOrder(root1) == self.leafOrder(root2)

def leafOrder(self, root):
    if root == None: 
        return []
    if root.left == None and root.right == None:
        return [root.val]
    return self.leafOrder(root.left) + self.leafOrder(root.right)