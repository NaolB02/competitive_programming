# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        summ = 0
        
        def dfs(node):
            nonlocal summ
            
            path.append(str(node.val))
            
            if not node.right and not node.left:
                num = ''.join(path)
                summ += int(num)
            
            elif not node.right:
                dfs(node.left)
            
            elif not node.left:
                dfs(node.right)
            
            else:
                dfs(node.right)
                dfs(node.left)
            
            path.pop()
        
        dfs(root)
        return summ
