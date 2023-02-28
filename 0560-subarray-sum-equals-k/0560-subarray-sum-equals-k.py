class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        count = 0
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]

            if curSum - k in prefix_sum:
                count += prefix_sum[curSum - k]
            
            if curSum in prefix_sum:
                prefix_sum[curSum] += 1
            
            else:
                prefix_sum[curSum] = 1
                  
        
        return count
            