class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preSum = [nums[0]]
        for i in range(1, len(nums)):
            preSum.append(nums[i] + preSum[i - 1])
        return preSum