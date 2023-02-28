class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        
        if rowIndex == 0 or rowIndex == 1:
            return row
        
        prevrow = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            row[i] = prevrow[i] + prevrow[i - 1]
        
        return row