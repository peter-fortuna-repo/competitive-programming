# Link to problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree


# Solution: 
# This solution uses a depth first search to find the paths to nodes p and q. 
# It then finds the first node that is in both paths. This is the lowest common
# ancestor.

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_to_p = []
        self.findPathToNode(root, p, path_to_p)

        path_to_q = []
        self.findPathToNode(root, q, path_to_q)

        path_to_p =set(path_to_p)
        for node in path_to_q[::-1]:
            if node in path_to_p:
                return node

    def findPathToNode(self, node: TreeNode, target: TreeNode, path: [TreeNode]) -> None:
        path.append(node)
        if node == target or node == None:
            return
        self.findPathToNode(node.left, target, path)
        if path[-1] == target:
            return
        path.pop()
        self.findPathToNode(node.right, target, path)
        if path[-1] == target:
            return
        path.pop()
        