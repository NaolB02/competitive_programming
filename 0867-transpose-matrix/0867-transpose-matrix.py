class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        newMatrix = [[0] * m for i in range(n)]
        print(newMatrix)
        
        for i in range(m):
            for j in range(n):
                newMatrix[j][i] = matrix[i][j]
        
        return newMatrix