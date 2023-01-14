class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralArr = []
        direction = "r"
        count = 0
        row, col = 0, 0
        m, n = len(matrix), len(matrix[0])
        
        while count < m * n:
            element = matrix[row][col]
            spiralArr.append(element)
            matrix[row][col] = 101
            
            if direction == "r":
                if col == n - 1 or matrix[row][col + 1] == 101:
                    direction = "d"
                    row += 1
                    
                else:
                    col += 1
            
            elif direction == "d":
                if row == m - 1 or matrix[row + 1][col] == 101:
                    direction = "l"
                    col -= 1
                
                else:
                    row += 1
            
            elif direction == "l":
                if col == 0 or matrix[row][col - 1] == 101:
                    direction = "u"
                    row -= 1
                
                else:
                    col -= 1
            
            elif direction == "u":
                if row == 0 or matrix[row - 1][col] == 101:
                    direction = "r"
                    col += 1
                
                else:
                    row -= 1
            
            count += 1
        
        return spiralArr