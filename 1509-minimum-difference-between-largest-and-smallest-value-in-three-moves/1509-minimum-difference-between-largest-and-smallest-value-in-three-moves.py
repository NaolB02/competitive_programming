class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 3, len(nums) - 1
        
        if len(nums) > 3:
            min_diff = math.inf
            
            while left >= 0:
                min_diff = min(min_diff, nums[right] - nums[left])
                left -= 1
                right -= 1
            
            return min_diff
        
        else:
            return 0