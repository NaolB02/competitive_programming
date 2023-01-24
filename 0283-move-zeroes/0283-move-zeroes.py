class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         holder = 0
#         r = 1
        
#         while holder < len(nums) and r < len(nums):
#             if nums[holder] == 0 and nums[r] != 0:
#                 nums[holder], nums[r] = nums[r], nums[holder]
                
#             if nums[holder] != 0:
#                 holder += 1
                
#             if nums[r] == 0 or r <= holder:
#                 r += 1
        
        holder = 0
        
        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
     
    