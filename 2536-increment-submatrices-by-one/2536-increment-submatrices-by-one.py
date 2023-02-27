class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        def get_prefix_sum(matrix):
            m = len(matrix)
            
            for row in range(m):
                for col in range(1, m):
                    matrix[row][col] += matrix[row][col - 1]
            
            for row in range(1, m):
                for col in range(m):
                    matrix[row][col] += matrix[row - 1][col]
            
            return matrix
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        for query in queries:
            row1, col1, row2, col2 = query
            
            matrix[row1][col1] += 1
        
            if row2 != n - 1 and col2 != n - 1:
                matrix[row2 + 1][col1] -= 1
                matrix[row1][col2 + 1] -= 1
                matrix[row2 + 1][col2 + 1] += 1
            
            elif row2 == n - 1 and col2 != n - 1:
                matrix[row1][col2 + 1] -= 1
            
            elif col2 == n - 1 and row2 != n - 1:
                matrix[row2 + 1][col1] -= 1
        
        return get_prefix_sum(matrix)
            