class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        hashmp = {}
        
        for num in nums:
            if k - num in hashmp:
                count += 1
                if hashmp[k - num] > 1:
                    hashmp[k - num] -= 1
                else:
                    del hashmp[k - num]
            
            else:
                hashmp[num] = hashmp.get(num, 0) + 1
        
        return count
        
        
        
        
        
        
        
#         nums.sort()
#         start, end = 0, len(nums) - 1
#         count = 0
        
#         while start < end:
#             curSum = nums[start] + nums[end]
            
#             if curSum < k:
#                 start += 1
            
#             elif curSum > k:
#                 end -= 1
            
#             else:
#                 count += 1
#                 start += 1
#                 end -= 1
        
#         return count
                
        