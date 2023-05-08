class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = defaultdict(int)
        graph = defaultdict(list)
        
        for i in range(numCourses):
            graph[i]
            dependencies[i]
            
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            dependencies[cur] += 1
        
        frontier = deque()
        for node in graph:
            if dependencies[node] == 0:
                frontier.append(node)
        
        topo_order = []
        while frontier:
            node = frontier.popleft()
            
            for neigh in graph[node]:
                dependencies[neigh] -= 1
                
                if dependencies[neigh] == 0:
                    frontier.append(neigh)
            
            topo_order.append(node)
            # del graph[node]
        
        if len(topo_order) != numCourses:
            return []
        return topo_order