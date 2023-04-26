# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        queue = [root]
        next_queue = []
        
        while queue:
            summ = 0
            for node in queue:
                summ += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            averages.append(summ / len(queue))
            queue = next_queue.copy()
            next_queue = []
        
        return averages