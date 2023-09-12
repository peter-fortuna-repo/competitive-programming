# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.

# Solution: 
# Simply recurse down the BST.

# Time complexity: O(log(n))  
# Space complexity: O(log(n)) 

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root == None or root.val == val:
        return root

    if val > root.val:
        return self.searchBST(root.right, val)
    else:
        return self.searchBST(root.left, val)