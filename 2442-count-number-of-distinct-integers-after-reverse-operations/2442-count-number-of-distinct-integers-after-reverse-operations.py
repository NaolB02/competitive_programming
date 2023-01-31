class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            revNum = str(nums[index])[::-1]
            nums.append(int(revNum))
        
        return len(set(nums))