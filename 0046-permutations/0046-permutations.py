class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur_per = []
        visited = (2 ** 6) - 1
        
        def backtrack():
            nonlocal visited
            if len(cur_per) == len(nums):
                permutations.append(cur_per[:])
                return
            
            for i in range(len(nums)):
                off_on = (visited >> i) & 1
                
                if off_on:
                    turn_off = 1 << i
                    visited ^= turn_off
                    cur_per.append(nums[i])
                    
                    backtrack()
                    
                    cur_per.pop()
                    turn_off = 1 << i
                    visited |= turn_off
            return
    
        backtrack()
        return permutations