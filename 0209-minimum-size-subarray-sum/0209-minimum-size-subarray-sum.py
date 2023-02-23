class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1, p2, sum, min_len = 0,-1, 0, 0

        while p2 < len(nums):

            if sum < target:
                p2 += 1
                if p2 < len(nums):
                    sum += nums[p2]
                

            else:
                if min_len == 0 or min_len > (p2 - p1 + 1):
                    min_len = p2 - p1 + 1
                sum -= nums[p1]
                p1 += 1
        
        return min_len
