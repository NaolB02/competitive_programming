class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        toeplitz = True
        diagonals = defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        
        for rowNum in range(m):
            for colNum in range(n):
                diagonals[rowNum - colNum].append(matrix[rowNum][colNum])
        
        for key in diagonals:
            if len(set(diagonals[key])) != 1:
                toeplitz = False
                break
        
        return toeplitz