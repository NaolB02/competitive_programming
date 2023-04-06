class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1 = edges[0]
        edge2 = edges[1]
        
        edge = edge1 + edge2
        edge = Counter(edge)
        
        for i in edge:
            if edge[i] == 2:
                return i