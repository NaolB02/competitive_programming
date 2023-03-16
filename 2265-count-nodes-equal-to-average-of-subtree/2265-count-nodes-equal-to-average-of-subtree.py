# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        final_count = {0: 0}
        
        def compareAverage(root):
            if not root.left and not root.right:
                final_count[0] += 1
                return [root.val, 1]
            
            elif not root.left:
                right = compareAverage(root.right)
                average = (root.val + right[0]) // (right[1] + 1)
                
                if average == root.val:
                    final_count[0] += 1
                    
                return [root.val + right[0], 1 + right[1]]
            
            elif not root.right:
                left = compareAverage(root.left)
                average = (root.val + left[0]) // (left[1] + 1)
                
                if average == root.val:
                    final_count[0] += 1
                    
                return [root.val + left[0], 1 + left[1]]
            
            else:
                left = compareAverage(root.left)
                right = compareAverage(root.right)
                average = (root.val + left[0] + right[0]) // (left[1] + 1 + right[1])
                
                if average == root.val:
                    final_count[0] += 1
                    
                return [root.val + left[0] + right[0], 1 + left[1] + right[1]]
        
        compareAverage(root)
        return final_count[0]