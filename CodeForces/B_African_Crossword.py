n, m = map(int, input().split())
matrix, crossed = [], []

for _ in range(n):
    matrix.append(input())
    crossed.append([0] * m)

for r in range(n):
    for c in range(m):
        letter = matrix[r][c]

        # check dups in the current row
        for new_c in range(c + 1, m):
            cur = matrix[r][new_c]

            if cur == letter:
                crossed[r][c] = 1
                crossed[r][new_c] = 1
        
        # check dups in the current column
        for new_r in range(r + 1, n):
            cur = matrix[new_r][c]

            if cur == letter:
                crossed[r][c] = 1
                crossed[new_r][c] = 1

result = []
for r in range(n):
    for c in range(m):
        letter = matrix[r][c]

        if crossed[r][c]:
            continue

        result.append(letter)

print("".join(result))