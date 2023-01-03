class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        countOfEqualPairs = 0
        # This dictionary stores tuple form of the rows and their occurences
        rowDict = defaultdict(int)
        # This dictionary stores tuple form of the columns and their occurences
        colDict = defaultdict(int)
        
        for row in grid:
            rowDict[tuple(row)] += 1
        
        for colNum in range(size):
            column = []
            
            for rowNum in range(size):
                column.append(grid[rowNum][colNum])
            
            colDict[tuple(column)] += 1
        
        # This block checks if a tuple is both a row and column
        for tup in rowDict:
            if tup in colDict:
                # The number of possible pairs is calculated
                countOfEqualPairs += (rowDict[tup] * colDict[tup])
        
        return countOfEqualPairs