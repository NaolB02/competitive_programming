from collections import Counter

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

sources = [False] * n
sinks = [False] * n
for i, row in enumerate(matrix):
    if len(Counter(row)) == 1:
        sinks[i] = True

for c in range(n):
    init = matrix[0][1]

    for r in range(n):
        cur = matrix[r][c]

        if cur != init:
            break
    
    if cur == init:
        sources[c] = True

so_count, so_nodes = 0, []
for i in range(n):
    if sources[i]:
        so_count += 1
        so_nodes.append(i + 1)

si_count, si_nodes = 0, []
for i in range(n):
    if sinks[i]:
        si_count += 1
        si_nodes.append(i + 1)

print(so_count, *so_nodes)
print(si_count, *si_nodes)
