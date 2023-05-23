class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        new_graph = {i:[] for i in range(len(graph))}
        dependencies = [len(i) for i in graph]
        
        for node, neighs in enumerate(graph):
            for neigh in neighs:
                new_graph[neigh].append(node)
        
        queue = deque()
        for i, dep in enumerate(dependencies):
            if dep == 0:
                queue.append(i)
        
        safe_nodes = []
        while queue:
            parent = queue.pop()
            safe_nodes.append(parent)
            
            for neigh in new_graph[parent]:
                dependencies[neigh] -= 1
                
                if dependencies[neigh] == 0:
                    queue.append(neigh)
        
        return sorted(safe_nodes)