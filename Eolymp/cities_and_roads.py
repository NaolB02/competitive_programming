n = int(input())
roads = 0
visited = set()

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        if row[j] == 1 and (i, j) not in visited:
            roads += 1
            visited.add((i, j))
            visited.add((j, i))

print(roads)
