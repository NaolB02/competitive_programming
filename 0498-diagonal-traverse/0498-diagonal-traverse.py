class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        # there are m + n - 1 diagonals in any matrix of size m x n
        # stores the individual diagonals
        diagonals = [[] for _ in range(m + n - 1)]
        diagonalArray = []
        
        for row in range(m):
            for col in range(n):
                diagonals[row + col].append(mat[row][col])
        
        for index in range(len(diagonals)):
            # the matrix is both traversed up and down alternatively
            # so even matrices are traversed down
            if index % 2 == 0:
                diagonals[index].reverse()
            
            for element in diagonals[index]:
                diagonalArray.append(element)
            
        return diagonalArray
        
       