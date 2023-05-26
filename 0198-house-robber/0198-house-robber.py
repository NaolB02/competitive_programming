class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(n):
            if n >= len(nums):
                return 0
            
            if n not in memo:
                memo[n] = nums[n] + max(dp(n + 2), dp(n + 3))
            
            return memo[n]
        
        return max(dp(0), dp(1))