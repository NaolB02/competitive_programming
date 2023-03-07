# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif not p or not q:
                return False

            check_val = p.val == q.val
            check_l_r = isSameTree(p.left, q.right)
            check_r_l = isSameTree(p.right, q.left)

            return check_l_r and check_r_l and check_val
    
        return isSameTree(root.left, root.right)