from collections import Counter

n = int(input())

for _ in range(n):
    numberOfPlanets, c = input().split()
    numberOfPlanets , c = int(numberOfPlanets), int(c)

    orbits = Counter(list(map(int, input().split())))
    minCost = 0

    for orbit in orbits:
        minCost += min(orbits[orbit], c)
    
    print(minCost)
