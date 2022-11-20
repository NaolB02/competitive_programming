class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        curmax = len(arr)
        curindex = arr.index(curmax)
        out = []
        
        while True:
            if curmax == 1 and curindex == 0:
                break
            
            elif curindex == 0 and curmax != 1:
                out.append(curmax)
                arr[0:curmax] = reversed(arr[0:curmax])
                curmax -= 1
                curindex = arr.index(curmax)
            
            else:
                out.append(curindex + 1)
                arr[0:curindex + 1] = reversed(arr[0:curindex + 1])
                curindex = arr.index(curmax)
        
        return out