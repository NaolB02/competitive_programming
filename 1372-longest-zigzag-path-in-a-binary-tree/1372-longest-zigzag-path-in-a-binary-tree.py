# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_count = 0
        
        def dfs(node, direction, count):
            nonlocal max_count
            
            if not node:
                return
            
            max_count = max(count, max_count)
            
            if direction == 'r':
                if node.right:
                    count += 1
                    dfs(node.right, 'l', count)
                    count -= 1
                
                dfs(node.left, 'r', 1)
                
            elif direction == 'l':
                if node.left:
                    count += 1
                    dfs(node.left, 'r', count)
                    count -= 1
                
                dfs(node.right, 'l', 1)
        
        dfs(root.left, 'r', 1)
        dfs(root.right, 'l', 1)
        return max_count