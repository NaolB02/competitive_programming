class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # sorting nums cyclically
        for i in range(len(nums)):
            cur = nums[i]
            while cur != (i + 1) and nums[cur - 1] != cur:
                nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
                cur = nums[i]
        
        # finding the numbers that disappeared
        not_present = []
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                not_present.append(i + 1)
        
        return not_present
                