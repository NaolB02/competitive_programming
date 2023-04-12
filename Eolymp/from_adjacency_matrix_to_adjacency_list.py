n = int(input())
graph = {}

for i in range(n):
    graph[i + 1] = []
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j]:
            graph[i + 1].append(j + 1)

for node in graph:
    print(len(graph[node]), end=' ')
    print(*graph[node])
