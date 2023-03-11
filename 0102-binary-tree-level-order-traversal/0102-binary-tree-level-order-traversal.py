# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverser(root):
            if not root:
                return 0
            
            left_depth = traverser(root.left)
            right_depth = traverser(root.right)
            
            return max(left_depth, right_depth) + 1
    
        num_of_levels = traverser(root)
        levels = [[] for _ in range(num_of_levels)]
        
        def level_traverser(root, level = 0):
            if not root or level > num_of_levels - 1:
                return
            
            levels[level].append(root.val)
            level_traverser(root.left, level + 1)
            level_traverser(root.right, level + 1)
        
        level_traverser(root)
        return levels