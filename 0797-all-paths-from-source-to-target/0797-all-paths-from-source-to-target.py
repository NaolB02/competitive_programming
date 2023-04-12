class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        dest = len(graph) - 1
        paths = []
        
        def dfs(node, path):
            nonlocal dest
            
            if node == dest:
                paths.append(path[:])
                return
                
            for neigh in graph[node]:
                path.append(neigh)
                dfs(neigh, path)
                path.pop()
        
        dfs(source, [source])
        return paths