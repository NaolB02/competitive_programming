class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # sorting nums cyclically
        for i in range(len(nums)):
            cur = nums[i]
            while cur != (i + 1) and nums[cur - 1] != cur:
                nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
                cur = nums[i]
        
        # finding the numbers are duplicates
        duplicates = []
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                duplicates.append(nums[i])
        
        return duplicates