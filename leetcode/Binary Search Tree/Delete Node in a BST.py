# Given a root node reference of a BST and a key, delete the node with the 
# given key in the BST. Return the root node reference (possibly updated) of 
# the BST.

# Basically, the deletion can be divided into two stages:
# 1. Search for a node to remove.
# 2. If the node is found, delete the node.

# Solution 1: Replace with left node
# Recurse down the BST to find the target node, then adjust the tree as needed.
# I chose to replace the deleted node with the left node each time, which was 
# challenging to implement and lead to many corner cases. The most signifigant 
# corner case involves moving the subtree of the replacement node, which is 
# moved to the right child's leftmost position.

# Time complexity: O(n)  
# Space complexity: O(1)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, node = self.findNode(root, key)
        if node == None:
            return root
        
        # The node that will replace our deleted node
        replacement = None
        if node.left != None: replacement = node.left
        elif node.right != None: replacement = node.right

        # Edge case - delete leaf node
        if parent and replacement == None:
            if parent.left == node: parent.left = None
            else: parent.right = None
            return root

        # Edge case - delete root without children
        if parent == None and replacement == None:
            root = None
            return root

        # Check for subtree that needs moving
        subtree = None
        if replacement == node.left and node.right != None:
            subtree = replacement.right

        # Adjust tree
        if parent:
            if parent.left == node:
                parent.left = replacement
            else:
                parent.right = replacement
        
        else:
            root = replacement
        
        if node.left == replacement and node.right:
            replacement.right = node.right
            temp = node.right
            while temp.left != None:
                temp = temp.left
            temp.left = subtree

        return root

    def findNode(self, root, key):
        parent = None
        node = root
        while node != None:
            if node.val == key:
                break
            parent = node

            if node.val > key:
                node = node.left
            else:
                node = node.right
        return parent, node
    

# Solution 2: Replace with predecessor node
# Similar to my previous algorithm, but streamlined in many ways. When the node
# is removed and replaced with it's predecessor (or successor), the delete
# operation is simlplified. The runtimes are effectively the same. Extra memory
# may be needed to make recursive calls.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right: return root.left
            if not root.left: return root.right

            predecessor = root.left
            while predecessor.right != None:
                predecessor = predecessor.right
            root.val = predecessor.val
            root.left = self.deleteNode(root.left, predecessor.val)
                
        return root