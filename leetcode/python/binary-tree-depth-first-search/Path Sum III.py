# Link to problem: https://leetcode.com/problems/path-sum-iii


# Solution: 
# This solution uses a recursive depth first search and uses a list to keep
# track of all the possible parents a path to that node could have. Each node
# loops through roughly log(n) possible parent nodes, so the resulting runtime
# is O(nlog(n))

# Time complexity: O(nlog(n)) 
# Space complexity: O(n)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.pathSumHelper(root, [targetSum])

    def pathSumHelper(self, root: Optional[TreeNode], target_sums: List[int]) -> int:
        num_paths = 0
        if root == None:
            return num_paths
        original_target = target_sums[-1]
        target_sums = [target_sum - root.val for target_sum in target_sums]

        for target_sum in target_sums:
            if target_sum == 0:
                num_paths += 1
        
        target_sums.append(original_target)

        num_paths += self.pathSumHelper(root.left, target_sums)
        num_paths += self.pathSumHelper(root.right, target_sums)

        return num_paths