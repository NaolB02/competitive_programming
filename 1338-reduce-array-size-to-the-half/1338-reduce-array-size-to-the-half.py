class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrDict = Counter(arr)
        pairArr = []
        n = len(arr)
        
        for key in arrDict:
            pairArr.append([key, arrDict[key]])
        
        print(pairArr)
        
        pairArr.sort(key = lambda x: x[1])
        
        out = 0        
        while n > int(len(arr) / 2):
            popped = pairArr.pop()
            n -= popped[1]
            out += 1
        
        return out