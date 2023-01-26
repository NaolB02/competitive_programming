class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def ValidityChecker(arr):
            arr = Counter(arr)
            if "." in arr:
                del arr["."]
            
            for num in arr:
                if arr[num] > 1:
                    return False
            
            return True
                
        for rowNum in range(9):
            curRow = board[rowNum]
            if not ValidityChecker(curRow):
                return False
        
        for colNum in range(9):
            curCol = []
            
            for rowNum in range(9):
                curCol.append(board[rowNum][colNum])
            
            if not ValidityChecker(curCol):
                return False
            
        for matRow in range(0, 9, 3):
            for matCol in range(0, 9, 3):
                matrix3x3 = []
                
                for i in range(3):
                    matrix3x3.extend(board[matRow + i][matCol: matCol + 3])
                    print(matrix3x3)
                
                if not ValidityChecker(matrix3x3):
                    return False
            
        return True