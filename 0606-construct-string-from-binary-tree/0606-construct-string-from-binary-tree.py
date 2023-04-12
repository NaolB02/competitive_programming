# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        bin_to_str = ''
        
        def dfs(node):
            nonlocal bin_to_str
                        
            if not node:
                return
        
            bin_to_str += str(node.val)
            
            # check if the node is a leaf node
            if not node.left and not node.right:
                return
            
            # add the left part to the string
            bin_to_str += '('
            dfs(node.left)
            bin_to_str += ')'
            
            if not node.right:
                return
            
            # add the right part to the string
            bin_to_str += '('
            dfs(node.right)
            bin_to_str += ')'
        
        dfs(root)
        return bin_to_str
