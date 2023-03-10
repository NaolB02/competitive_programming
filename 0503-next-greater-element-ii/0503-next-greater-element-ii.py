class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_greater = [10 ** 9 + 1] * len(nums)
        mon_stack = []
        
        for i in range(2 * len(nums)):
            i = i % len(nums)
            
            while mon_stack and nums[mon_stack[-1]] < nums[i]:
                popped_i = mon_stack.pop()
                next_greater[popped_i] = nums[i]
            
            mon_stack.append(i)
        
        for i in range(len(next_greater)):
            if next_greater[i] == 10 ** 9 + 1:
                next_greater[i] = -1
                
        return next_greater