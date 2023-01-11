class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numsDict = {}
        
        for index, num in enumerate(nums):
            numsDict[num] = index
        
        for op in operations:
            index = numsDict[op[0]]
            del numsDict[op[0]]
            numsDict[op[1]] = index
        
        modifiedArr = [0] * len(nums)
        for num in numsDict:
            index = numsDict[num]
            modifiedArr[index] = num
        
        return modifiedArr