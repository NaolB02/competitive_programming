# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        paths_sum = {0: 1}
        
        def dfs(node, summ):
            nonlocal count
            nonlocal targetSum
            
            if not node:
                return
            
            summ += node.val
            
            if summ - targetSum in paths_sum:
                count += paths_sum[summ - targetSum]
            
            paths_sum[summ] = paths_sum.get(summ, 0) + 1
            
            dfs(node.left, summ)
            dfs(node.right, summ)
            
            paths_sum[summ] -= 1
        
        dfs(root, 0)
        return count