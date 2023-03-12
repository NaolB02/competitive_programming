# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverser(root):
            if not root:
                return 0

            left_depth = traverser(root.left)
            right_depth = traverser(root.right)

            return max(left_depth, right_depth) + 1

        num_of_levels = traverser(root)
        right_side = [0] * num_of_levels
        if root:
            right_side[0] = root.val
        
        def get_right_side(root, level):
            if not root:
                return
            
            left = get_right_side(root.left, level + 1)
            right = get_right_side(root.right, level + 1)
            
            if root.right:
                right_side[level] = root.right.val
            
            elif root.left:
                right_side[level] = root.left.val
        
        get_right_side(root, 1)
        return right_side
