from collections import defaultdict

numOfTestcases = int(input())

for _ in range(numOfTestcases):
    m, n = map(int, input().split())
    matrix = []

    for r in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    topBotttomD = defaultdict(int)
    bottomTopD = defaultdict(int)

    for rowNum in range(m):
        for colNum in range(n):
            topBotttomD[rowNum - colNum] += matrix[rowNum][colNum]
            bottomTopD[rowNum + colNum] += matrix[rowNum][colNum]
    
    maxSum = 0
    for rowNum in range(m):
        for colNum in range(n):
            curSum = topBotttomD[rowNum - colNum] + bottomTopD[rowNum + colNum] - matrix[rowNum][colNum]
            maxSum = max(curSum, maxSum)

    print(maxSum)
