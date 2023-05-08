class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        color = {i: 'w' for i in range(numCourses)}
        
        
#         for i in range(numCourses):
#             graph[i]
#             dependencies[i]
            
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            dependencies[cur] += 1
        
        components = []
        for node in graph:
            if dependencies[node] == 0:
                components.append(node)
        
        stack = []
        isCyclic = False
        def dfs(node):
            nonlocal isCyclic
            
            if color[node] == 'b':
                return
            
            if color[node] == 'g':
                isCyclic = True
                return
            
            if len(graph[node]) == 0:
                color[node] = 'b'
                stack.append(node)
                return True
            
            color[node] = 'g'
            for neigh in graph[node]:
                dfs(neigh)
                
                if isCyclic:
                    return
            
            color[node] = 'b'  
            stack.append(node)
            
        # print('frontier: ', frontier)
        for node in components:
            dfs(node)
            # print(graph, color)
            
        if len(stack) != numCourses:
            return []
        
        return stack[::-1]