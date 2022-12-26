class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        
        for index in range(len(nums)):
            for index2 in range(index + 1, len(nums)):
                if nums[index] == nums[index2]:
                    pairs += 1
                    
        return pairs