class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElement = arr[-1]
        arr[-1] = -1
        
        for index in range(len(arr) - 2, -1, -1):
            curMax = maxElement
            if arr[index] > maxElement:
                maxElement = arr[index]
            
            arr[index] = curMax
        
        return arr