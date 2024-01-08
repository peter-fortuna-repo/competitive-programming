# Link to problem: https://leetcode.com/problems/range-sum-of-bst/description/?envType=daily-question&envId=2024-01-08

# Solution: DFS
# A straightforward application of a DFS, where the value of each node is added 
# only if it is between high and low

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + (root.val if (root.val >= low and root.val <= high) else 0)