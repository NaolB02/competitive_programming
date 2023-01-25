class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        k = 1
        
#         for right in range(len(nums)):
#             if nums[right] != nums[left]:
#                 left += 1
#                 nums[left] = nums[right]
#                 k += 1
        
#         return k
        
        for right in range(1, len(nums)):
            if nums[right] == nums[left]:
                nums[right] = "_"
            
            else:
                left = right
                k += 1
                
        holder = 0
        
        for seeker in range(len(nums)):
            if nums[seeker] != "_":
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
        
        return k
    