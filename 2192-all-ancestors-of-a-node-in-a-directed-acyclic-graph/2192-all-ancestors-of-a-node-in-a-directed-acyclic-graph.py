class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i: [] for i in range(n)}
        dependencies = [0] * n
        
        for src, dest in edges:
            graph[src].append(dest)
            dependencies[dest] += 1
        
        queue = deque()
        for i in range(n):
            if dependencies[i] == 0:
                queue.append(i)
        
        parents = [set() for i in range(n)]
        while queue:
            parent = queue.popleft()
            
            for neigh in graph[parent]:
                dependencies[neigh] -= 1
                
                if dependencies[neigh] == 0:
                    queue.append(neigh)
                
                parents[neigh] = parents[neigh].union(parents[parent])
                parents[neigh].add(parent)
        
        for i in range(n):
            parents[i] = sorted(parents[i])
        
        return parents