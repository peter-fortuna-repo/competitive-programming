# Given the root of a binary tree, imagine yourself standing on the right side 
# of it, return the values of the nodes you can see ordered from top to bottom.

# Solution: 
# To get the right side view, we do a BFS and one level at a time and keep 
# track of the right-most node on each level.

# Time complexity: O(n)  
# Space complexity: O(n) 

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root==None:
        return

    right_side = []
    next_level = [root]
    side_view = [root.val]
    while next_level:
        current_level = next_level
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if next_level:
            side_view.append(next_level[-1].val)

    return side_view