# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        
        def find_freq(root):
            if not root:
                return
            
            freq[root.val] += 1
            find_freq(root.left)
            find_freq(root.right)
        
        find_freq(root)
        max_freq = max(freq.values())
        modes = []
        
        for key in freq:
            if freq[key] == max_freq:
                modes.append(key)
        
        return modes