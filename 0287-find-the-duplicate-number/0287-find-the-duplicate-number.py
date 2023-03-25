class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sorting nums cyclically
        for i in range(len(nums)):
            cur = nums[i]
            while cur != (i + 1): 
                if nums[cur - 1] == cur:
                    return cur
                
                nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
                cur = nums[i]