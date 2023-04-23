# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        node = TreeNode(preorder[0])
        
        preorder.pop(0)
        sorted_pre = sorted(preorder)
        index = bisect_left(preorder, node.val)
        
        node.left = self.bstFromPreorder(preorder[:index])
        node.right = self.bstFromPreorder(preorder[index:])
        
        return node
        
        
        
        
        # root = TreeNode(preorder[0])
        # stack = [[1001, preorder[0]]]
        # i = 1
        
#         def dfs(node):
#             nonlocal i
            
#             if preorder[i] < node.val:
#                 node.left = TreeNode(preorder[i])
#                 stack.append([node.val, preorder[i]])
#                 i += 1
                
#                 dfs(node.left)
            
#             if stack[-1] > preorder[i] > node.val:
#                 node.right = TreeNode(preorder[i])
#                 stack.append([node.val, preorder[i]])
#                 i += 1
                
#                 dfs(node.right)
                
#             if preorder[i] > stack[-1] and preorder[i] > node.val:
                