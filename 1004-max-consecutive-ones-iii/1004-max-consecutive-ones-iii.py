class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        temp = k
        l = 0
        maxSize = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                temp -= 1
            
            while temp == -1:
                if nums[l] == 0:
                    temp += 1
                l += 1
            
            maxSize = max(maxSize, r - l + 1)
    
        return maxSize
        