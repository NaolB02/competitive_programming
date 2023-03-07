# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def inorderTraversal(root):
            if not root.left:
                return root.val

            return inorderTraversal(root.left)
        
        if not root:
            return root
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            newVal = inorderTraversal(root.right)
            root.val = newVal
            root.right = self.deleteNode(root.right, newVal)
        
        return root
        