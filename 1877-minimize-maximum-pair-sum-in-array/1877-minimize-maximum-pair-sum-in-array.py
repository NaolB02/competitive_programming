class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        maxSum = 0
        
        while r > l:
            summ = nums[l] + nums[r]
            maxSum = max(maxSum, summ)
            l += 1
            r -= 1
        
        return maxSum