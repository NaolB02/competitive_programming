class Solution:
    def checkMagicSquare(self, grid: List[List[int]], row: int, col: int) -> bool:
        if len(grid) - row < 3 or len(grid[0]) - col < 3:
            return False
        
        matrix = set(grid[row][col: col + 3]).union(set(grid[row + 1][col: col + 3]).union(set(grid[row + 2][col: col + 3])))
        if len(matrix) < 9 or 0 in matrix or max(matrix) > 9:
            return False
        
        i = 1
        for r in range(row, row + 3):
            summ = 0
            
            for c in range(col, col + 3):
                summ += grid[r][c]
            
            if i == 1:
                pre_summ = summ
                i += 1
                continue
            
            elif summ != pre_summ:
                return False
        
        for c in range(col, col + 3):
            summ = 0
            
            for r in range(row, row + 3):
                summ += grid[r][c]
            
            if summ != pre_summ:
                return False
        
        diag1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
        diag2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
        
        if diag1 != pre_summ or diag2 != pre_summ:
            return False
        
        return True
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.checkMagicSquare(grid, r, c):
                    count += 1
        
        return count
        