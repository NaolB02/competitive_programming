class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i: [] for i in range(n)}
        dependencies = [0] * n
        
        for src, dest in richer:
            graph[src].append(dest)
            dependencies[dest] += 1
        
        queue = deque()
        for i in range(n):
            if dependencies[i] == 0:
                queue.append(i)
        
        answer = [i for i in range(n)]
        while queue:
            parent = queue.popleft()
            
            for neigh in graph[parent]:
                dependencies[neigh] -= 1
                
                if dependencies[neigh] == 0:
                    queue.append(neigh)
                
                answer[neigh] = answer[parent] if quiet[parent] < quiet[neigh] else answer[neigh]
                quiet[neigh] = quiet[parent] if quiet[parent] < quiet[neigh] else quiet[neigh]
                        
        return answer