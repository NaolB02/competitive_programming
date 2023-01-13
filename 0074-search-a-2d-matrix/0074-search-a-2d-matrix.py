class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        first = 0
        last = rowLen * colLen - 1
        
        while first <= last:
            mid = (first + last) // 2
            midRow = mid // colLen
            midCol = mid % colLen
            
            if target == matrix[midRow][midCol]:
                return True
            
            elif target > matrix[midRow][midCol]:
                first = mid + 1
            
            else:
                last = mid - 1
        
        
        
        
        