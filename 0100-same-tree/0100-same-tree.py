# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        check_val = p.val == q.val
        check_left = self.isSameTree(p.left, q.left)
        check_right = self.isSameTree(p.right, q.right)
        
        return check_left and check_right and check_val