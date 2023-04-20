# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs2(node, 0)
            dfs(node.left)
            dfs(node.right)
        
        def dfs2(node, summ):
            nonlocal targetSum
            nonlocal count
            
            if not node:
                return
            
            summ += node.val
            
            if summ == targetSum:
                count += 1
                
            dfs2(node.left, summ)
            dfs2(node.right, summ)
            summ -= node.val
        
        dfs(root)
        return count