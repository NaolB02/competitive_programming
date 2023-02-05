class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        # transposing the matrix
        for rowNum in range(size):
            for colNum in range(rowNum, size):
                # swapping the elements
                matrix[rowNum][colNum], matrix[colNum][rowNum] = matrix[colNum][rowNum], matrix[rowNum][colNum]
            
        # reversing every row
        for rowNum in range(size):
            matrix[rowNum].reverse()