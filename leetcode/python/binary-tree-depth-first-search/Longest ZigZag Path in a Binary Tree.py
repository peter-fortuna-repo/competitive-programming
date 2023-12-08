# Link to problem: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree


# Solution: Check each zigzag at each node
# This solution goes through all nodes and calls the maxZigZag function on 
# them. This function returns the maximum length zigzag that starts at that
# node.

# Time complexity:O(n^2) (nlog(n) average)
# Space complexity: O(1)

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            longest = max(longest, self.zigZag(node, 1), self.zigZag(node, -1))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return longest


    def maxZigZag(self, node: TreeNode, direction: int) -> int:
        length = 0
        while self.canZigZag(node, direction):
            if direction == 1:
                node = node.right
            else:
                node = node.left
            length += 1
            direction *= -1

        return length

    def canZigZag(self, node: TreeNode, direction: int) -> bool:
        if direction == 1 and node.right != None:
            return True
        elif direction == -1 and node.left != None:
            return True
        return False
    

# Solution: 
# This solution uses a recursive depth first search and tracks the maximum of
# all possible zigzags in one pass through all nodes.

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[2]
    
    def dfs(self, node: Optional[TreeNode]) -> tuple:
        if not node:
            return (-1,-1,-1)
        left, right = self.dfs(node.left), self.dfs(node.right)
        return (left[1]+1, right[0]+1, max(left[1]+1, right[0]+1, left[2], right[2]))