# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeToGraph(self,  root: TreeNode) -> dict:
        graph = defaultdict(list)
        fringe = deque([root])
        
        while fringe:
            parent = fringe.popleft()
            left, right = parent.left, parent.right
            
            if left:
                graph[parent.val].append(left.val)
                graph[left.val].append(parent.val)
                fringe.append(left)
            
            if right:
                graph[parent.val].append(right.val)
                graph[right.val].append(parent.val)
                fringe.append(right)
        
        return graph
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = self.treeToGraph(root)
        fringe = deque([[target.val, 0]])
        visited = set([target.val])
        nodesK = []
        
        while fringe:
            node, distance = fringe.popleft()
            
            if distance == k:
                nodesK.append(node)
            
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    fringe.append([neigh, distance + 1])
        
        return nodesK
     