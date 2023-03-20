# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        leftmost = 0
        rightmost = 0
        
        def assigner(row, col, root):
            nonlocal leftmost
            nonlocal rightmost
            
            if not root:
                return 
          
            leftmost = min(leftmost, col)
            rightmost = max(rightmost, col)
            ans[(row, col)].append(root.val)
            
            assigner(row + 1, col - 1, root.left)
            assigner(row + 1, col + 1, root.right)
        
        assigner(0, 0, root)
        out = [[] for _ in range(rightmost - leftmost + 1)]
        
        sorted_ans = sorted(ans.items(), key=lambda x:x[0][0])
        for key in range(len(sorted_ans)):
            sorted_ans[key][1].sort()
            out[sorted_ans[key][0][1] - leftmost] += sorted_ans[key][1]
            
        return out
            