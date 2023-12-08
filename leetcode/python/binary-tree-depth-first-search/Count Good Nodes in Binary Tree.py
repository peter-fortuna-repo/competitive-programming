# Given a binary tree root, a node X in the tree is named good if in the path 
# from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution: 
# We do a DFS down the tree, keeping track of the maximum value of the node's
# ancestors. In each recursive call, we return the number of good nodes on the 
# left subtree, plus the number of good nodes on the right subtree, plus one if
# our node is good.

# Time complexity: O(n)  
# Space complexity: O(n) 

def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -10000)

def dfs(self, root: TreeNode, max_val: int) -> int:
    if root == None:
        return 0        
    is_good = 0
    if root.val >= max_val: 
        is_good = 1
        max_val = root.val
    return is_good + self.dfs(root.left, max_val) + self.dfs(root.right, max_val)