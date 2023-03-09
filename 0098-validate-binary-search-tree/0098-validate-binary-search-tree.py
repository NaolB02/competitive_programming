# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate_BST(root):
            if not root.left and not root.right:
                return [root.val, root.val, True]
            
            elif not root.left:
                check_right = validate_BST(root.right)
                max_val = max(root.val, check_right[0])
                min_val = min(root.val, check_right[1])
                right= root.val < check_right[1]
                
                return [max_val, min_val, right and check_right[2]]
            
            elif not root.right:
                check_left = validate_BST(root.left)
                max_val = max(root.val, check_left[0])
                min_val = min(root.val, check_left[1])
                left = root.val > check_left[0]
                
                return [max_val, min_val, left and check_left[2]]
                
            check_right = validate_BST(root.right)
            check_left = validate_BST(root.left)
            max_val = max(root.val, check_right[0], check_left[0])
            min_val = min(root.val, check_right[1], check_left[1])
            
            right= root.val < check_right[1]
            left = root.val > check_left[0]
            
            return [max_val, min_val, right and left and check_right[2] and check_left[2]]
        
        return validate_BST(root)[2]