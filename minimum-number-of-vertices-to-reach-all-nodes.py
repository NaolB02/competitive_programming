class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodesTo = set()
        nodesFrom = set()
        
        for fr, to in edges:
            nodesTo.add(to)
            
            if fr not in nodesTo:
                nodesFrom.add(fr)
            
            if to in nodesFrom:
                nodesFrom.remove(to)
        
        return list(nodesFrom)