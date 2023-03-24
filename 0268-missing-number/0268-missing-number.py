class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        
        for r in range(len(nums)):
            while nums[r] != -1 and nums[r] != r:
                ind = nums[r]
                nums[r], nums[ind] = nums[ind], nums[r]
            
        for i in range(len(nums)):
            if i != nums[i]:
                return i