class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for node, neigh in edges:
            graph[node].append(neigh)
            graph[neigh].append(node)
            
        def dfs(vertex, visited):
            nonlocal destination
            
            # base case
            if destination == vertex:
                return True
            
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    result = dfs(neighbour, visited)
                    
                    if result:
                        return True
        
        return dfs(source, set())
        