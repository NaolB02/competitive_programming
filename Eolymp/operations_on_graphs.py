class Graph:
    def __init__(self, n: int) -> None:
        self.graph = {}

        for i in range(n):
            self.graph[i + 1] = []
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def vertex(self, u):
        return self.graph[u]
    

n = int(input())
graph = Graph(n)
k = int(input())
for i in range(k):
    inst = list(map(int, input().split()))

    if inst[0] == 1:
        graph.addEdge(inst[1], inst[2])
    
    else:
       print(*graph.vertex(inst[1]))

