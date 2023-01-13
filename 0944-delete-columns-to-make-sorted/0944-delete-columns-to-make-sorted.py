class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedColumns = 0
        rowLength = len(strs)
        columnLength = len(strs[0])
        
        for colNum in range(columnLength):
            order = 0
            
            for rowNum in range(rowLength):
                letter = strs[rowNum][colNum]
                
                if ord(letter) < order:
                    deletedColumns += 1
                    break
                
                order = ord(letter)
        
        return deletedColumns