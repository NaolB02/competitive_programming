class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        total = 0
        
        for i, num in enumerate(nums):
            missing ^= num
            total ^= i
        
        total ^= len(nums)
        return missing ^ total