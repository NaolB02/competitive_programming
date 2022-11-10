class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmp = {}
        
        for i in range(len(nums)):
            if target - nums[i] in hashmp:
                return[hashmp[target - nums[i]], i]
            
            hashmp[nums[i]] = i