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
            if not root.left and not root.right:
                cur_path.append(str(root.val))
                paths.append("->".join(cur_path))
                cur_path.pop()
                return
            
            elif not root.left:
                cur_path.append(str(root.val))
                backtrack(root.right)
                cur_path.pop()
                
            
            elif not root.right:
                cur_path.append(str(root.val))
                backtrack(root.left)
                cur_path.pop()
            
            else:
                #case 1 - left
                cur_path.append(str(root.val))
                backtrack(root.left)
                cur_path.pop()

                #case 2 - right
                cur_path.append(str(root.val))
                backtrack(root.right)
                cur_path.pop()
        
        backtrack(root)
        return paths