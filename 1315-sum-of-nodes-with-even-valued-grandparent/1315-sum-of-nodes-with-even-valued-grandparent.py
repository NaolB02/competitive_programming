# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        summ = 0
        def dfs(grandparent, parent, child):
            nonlocal summ
            
            if child == None:
                return
            
            if grandparent % 2 == 0:
                summ += child.val
            
            # to the left
            dfs(parent, child.val, child.left)
            
            #to the right
            dfs(parent, child.val, child.right)
        
        dfs(1, 1, root)
        return summ