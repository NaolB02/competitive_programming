class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        def largestIn3x3(newMatrix, matrix, rowNum, colNum):
            centerRow = rowNum + 1
            centerCol = colNum + 1
            topMax = max(matrix[centerRow - 1][centerCol - 1], matrix[centerRow - 1][centerCol], matrix[centerRow - 1][centerCol + 1])
            
            middleMax = max(matrix[centerRow][centerCol - 1], matrix[centerRow][centerCol], matrix[centerRow][centerCol + 1])
            
            bottomMax = max(matrix[centerRow + 1][centerCol - 1], matrix[centerRow + 1][centerCol], matrix[centerRow + 1][centerCol + 1])
            
            newMatrix[rowNum].append(max(topMax, middleMax, bottomMax))
        
        generatedMatrix = [[] for _ in range(len(grid) - 2)]
    
    
        for rowNum in range(len(grid) - 2):
            for colNum in range(len(grid) - 2):
                largestIn3x3(generatedMatrix, grid, rowNum, colNum)
    
        return generatedMatrix
            