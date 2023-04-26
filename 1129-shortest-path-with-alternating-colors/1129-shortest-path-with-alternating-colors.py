class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # first list : red, second list: blue
        graph = {x: [[], []] for x in range(n)}
        visited = set()
        
        for src, dest in redEdges:
            graph[src][0].append(dest)
        
        for src, dest in blueEdges:
            graph[src][1].append(dest)
        
        distances = [401] * n
        queue = deque([(0, 0, 0), (0, 1, 0)])
        
        while queue:
            node, color, dist = queue.popleft()
            neighbours = graph[node][color]
            
            if (node, color) in visited:
                continue
                
            if distances[node] > dist:
                distances[node] = dist
            
            visited.add((node, color))
            for neighbour in neighbours:
                queue.append((neighbour, 1 - color, dist + 1))
        
        distances = [-1 if x==401 else x for x in distances]
        return distances