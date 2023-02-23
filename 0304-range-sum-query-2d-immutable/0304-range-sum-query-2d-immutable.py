class NumMatrix:

    def __init__(self, matrix: List[List[int]]):        
        for rowNum in range(len(matrix)):
            for colNum in range(len(matrix[0])):
                if rowNum != 0 and colNum != 0:
                    matrix[rowNum][colNum] += matrix[rowNum - 1][colNum]+ matrix[rowNum][colNum - 1]-matrix[rowNum - 1][colNum - 1]
                    
                elif rowNum == 0 and colNum == 0:
                    pass
                
                elif rowNum == 0:
                    matrix[rowNum][colNum] += matrix[rowNum][colNum - 1]
                
                elif colNum == 0:
                    matrix[rowNum][colNum] += matrix[rowNum - 1][colNum]
            
        self.matrix = matrix
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        
        if row1 != 0 and col1 != 0:
            return matrix[row2][col2] - matrix[row1 - 1][col2] - matrix[row2][col1 - 1] + matrix[row1 - 1][col1 - 1]
            
        elif row1 == 0 and col1 == 0:
            return matrix[row2][col2]

        elif row1 == 0:
            return matrix[row2][col2] - matrix[row2][col1 - 1] 

        elif col1 == 0:
            return matrix[row2][col2] - matrix[row1 - 1][col2]            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)