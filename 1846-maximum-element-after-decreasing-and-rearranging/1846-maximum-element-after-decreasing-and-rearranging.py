class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        start = 1
        for i in range(1, len(arr)):
            if arr[i] - start > 1:
                arr[i] = start + 1
            
            start = arr[i]
        
        if len(arr) == 1:
            return start
        return arr[-1]