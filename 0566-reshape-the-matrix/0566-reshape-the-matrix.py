class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        listOfMat  = []
        m, n = len(mat), len(mat[0])
        newMatrix = [[] for _ in range(r)]
        
        if r * c != m * n:
            return mat
        
        for rowNum in range(m):
            for colNum in range(n):
                listOfMat.append(mat[rowNum][colNum])
        
        index = 0
        for rowNum in range(r):
            for colNum in range(c):
                newMatrix[rowNum].append(listOfMat[index])
                index += 1
        
        return newMatrix