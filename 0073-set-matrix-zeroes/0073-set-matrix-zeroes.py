class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        # build columns 
        columns = [] 
        for colNum in range(n):
            columns.append([])
            
            for rowNum in range(m):
                columns[colNum].append(matrix[rowNum][colNum])
                
        # build rows
        rows = matrix.copy()
        
        # check for zeros and modify rows and columns
        for rowNum in range(m):
            for colNum in range(n):
                if matrix[rowNum][colNum] == 0:
                    rows[rowNum] = [0] * n
                    columns[colNum] = [0] * m
        
        # modify the matrix
        for rowNum in range(m):
            for colNum in range(n):
                if columns[colNum][rowNum] == 0:
                    matrix[rowNum][colNum] = 0
                
                if rows[rowNum][colNum] == 0:
                    matrix[rowNum][colNum] = 0
                    
        