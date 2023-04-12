"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        
        def dfs(node, cur_depth):
            nonlocal max_depth
            
            if not node:
                return
            
            cur_depth += 1
            max_depth = max(max_depth, cur_depth)
            
            for child in node.children:
                dfs(child, cur_depth)
            
            cur_depth -= 1
        
        dfs(root, 0)
        return max_depth