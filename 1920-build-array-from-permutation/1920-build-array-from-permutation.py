class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation = [0] * len(nums)
        
        for index in range(len(nums)):
            permutation[index] = nums[nums[index]]
        
        return permutation