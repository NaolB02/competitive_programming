class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        strictlyInc = True
        
        if len(arr) == 1 or arr[0] > arr[1] or arr[len(arr) - 2] < arr[len(arr) - 1]:
            return False
        
        for index in range(1, len(arr)):    
            if strictlyInc and arr[index - 1] < arr[index]:
                continue
            
            elif arr[index - 1] > arr[index]:
                strictlyInc = False
            
            else:
                return False
        
        return True
        
        