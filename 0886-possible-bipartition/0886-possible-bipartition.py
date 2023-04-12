class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        colors = [0] * n
        
        def dfs(node, color):
            if colors[node - 1] != 0:
                if colors[node - 1] == color:
                    return True
                
                return False
        
            colors[node - 1] = color
            for neigh in graph[node]:
                res = dfs(neigh, -color)
                
                if not res:
                    return False
            
            return True
            
        for node in graph:
            if colors[node - 1] == 0:
                res = dfs(node, 1)
                
                if not res:
                    return False
        
        return True
            