class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rowNum in range(9):
            curRow = board[rowNum]
            curRow = Counter(curRow)
            if "." in curRow:
                del curRow["."]
            
            for num in curRow:
                if curRow[num] > 1:
                    return False
        
        for colNum in range(9):
            curCol = []
            
            for rowNum in range(9):
                curCol.append(board[rowNum][colNum])
            
            curCol = Counter(curCol)
            if "." in curCol:
                del curCol["."]
            
            for num in curCol:
                if curCol[num] > 1:
                    return False
            
        for matRow in range(0, 9, 3):
            for matCol in range(0, 9, 3):
                matrix3x3 = []
                
                for i in range(3):
                    matrix3x3.extend(board[matRow + i][matCol: matCol + 3])
                    print(matrix3x3)
                
                matrix3x3 = Counter(matrix3x3)
                if "." in matrix3x3:
                    del matrix3x3["."]
                
                for num in matrix3x3:
                    if matrix3x3[num] > 1:
                        return False
        
        return True