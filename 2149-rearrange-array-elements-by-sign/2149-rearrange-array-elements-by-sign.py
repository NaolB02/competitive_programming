class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        j = 0
        k = 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                new_nums[j] = nums[i]
                j += 2
            
            else:
                new_nums[k] = nums[i]
                k += 2
    
        return new_nums
            