class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = self.or_everything(nums)
        count = 0
        cur_or = []
        
        def backtrack(i):
            nonlocal max_or, count, cur_or
            
            if self.or_everything(cur_or) == max_or:
                count += 2 ** (len(nums) - i)
                return
            
            if i == len(nums):
                return
            
            # choose logic
            cur_or.append(nums[i])
            backtrack(i + 1)
            cur_or.pop()
            
            # not choose logic
            backtrack(i + 1)
        
        backtrack(0)
        return count
    
    def or_everything(self, nums):
        all_or = 0
        for num in nums:
            all_or |= num
        
        return all_or