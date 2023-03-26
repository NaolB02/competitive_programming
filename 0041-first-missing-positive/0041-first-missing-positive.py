class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        -> cyclic approach
        # sorting nums cyclically
        for i in range(len(nums)):
            cur = nums[i]
            
            while cur != (i + 1) and cur in range(1, len(nums) + 1) and nums[cur - 1] != cur:
                nums[cur - 1], nums[i] = nums[i], nums[cur - 1]
                cur = nums[i]
        
        # searching for the first missing integer
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                return i + 1
        
        return i + 2
        '''
        
        freq = [0] * (len(nums) + 1)
        
        for num in nums:
            if num > 0 and num < len(nums) + 1:
                freq[num - 1] += 1
        
        for i in range(len(freq)):
            if freq[i] == 0:
                return i + 1