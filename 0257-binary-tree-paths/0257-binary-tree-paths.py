# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        cur_path = []
        
        def backtrack(root):
            cur_path.append(str(root.val))
            
            if not root.left and not root.right:
                paths.append("->".join(cur_path))
            
            elif not root.left:
                backtrack(root.right)   
            
            elif not root.right:
                backtrack(root.left)
            
            else:
                #case 1 - left
                backtrack(root.left)

                #case 2 - right
                backtrack(root.right)
            
            cur_path.pop()
            
        backtrack(root)
        return paths