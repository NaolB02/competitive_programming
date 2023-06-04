class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = {i: [] for i in range(n)}
        dependencies = [0] * n
        
        for src, dest in prerequisites:
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
        
        result = []
        for u, v in queries:
            result.append(u in parents[v])
        
        return result