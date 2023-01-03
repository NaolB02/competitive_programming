class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        countOfEqualPairs = 0
        rowDict = defaultdict(int)
        colDict = defaultdict(int)
        
        for row in grid:
            rowDict[tuple(row)] += 1
        
        for colNum in range(size):
            column = []
            
            for rowNum in range(size):
                column.append(grid[rowNum][colNum])
            
            colDict[tuple(column)] += 1
        
        for tup in rowDict:
            if tup in colDict:
                countOfEqualPairs += (rowDict[tup] * colDict[tup])
        
        return countOfEqualPairs