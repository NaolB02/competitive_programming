class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = []
        columns = []
        diff = []
        for _ in range(m):
            diff.append([])
        
        # calculates the difference of the ones and zeros for each row
        for row in range(m):
            onesRow = 0
            zerosRow = 0
            
            for col in range(n):
                element = grid[row][col]
                
                if element == 0:
                    zerosRow += 1
                
                else:
                    onesRow += 1
            
            rows.append(onesRow - zerosRow)
        
        # calculates the difference of the ones and zeros for each column
        for col in range(n):
            onesCol = 0
            zerosCol = 0
            
            for row in range(m):
                element = grid[row][col]
                
                if element == 0:
                    zerosCol += 1
                
                else:
                    onesCol += 1
            
            columns.append(onesCol - zerosCol)
        
        for rowNum in range(len(rows)):
            for colNum in range(len(columns)):
                diff[rowNum].append(rows[rowNum] + columns[colNum])
        
        return diff