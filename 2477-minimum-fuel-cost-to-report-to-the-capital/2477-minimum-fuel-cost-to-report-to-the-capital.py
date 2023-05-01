class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        
        for fro, to in roads:
            graph[fro].append(to)
            graph[to].append(fro)
            
        visited = set([0])
        litres = 0
        def fuel(node):
            nonlocal litres
            reps = 1
            
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    reps += fuel(neigh)
            
            litres += ceil(reps / seats)
            return reps
        
        for neigh in graph[0]:
            visited.add(neigh)
            fuel(neigh)
            
        return litres
            