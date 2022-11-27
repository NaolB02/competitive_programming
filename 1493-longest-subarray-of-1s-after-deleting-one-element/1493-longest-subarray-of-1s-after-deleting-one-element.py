class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        deleted = 0
        l = 0
        count = 0
        maxSize = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                deleted += 1
                   
            else:
                count += 1
                
            while deleted > 1:
                    if nums[l] == 0:
                        deleted -= 1
                    else:
                        count -= 1
                    l += 1

            maxSize = max(maxSize, count)
        
        if deleted == 0:
            maxSize -= 1

        return maxSize
