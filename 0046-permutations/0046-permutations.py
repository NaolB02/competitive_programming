class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur_per = []
        visited = set()
        
        def backtrack():
            if len(cur_per) == len(nums):
                permutations.append(cur_per[:])
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    cur_per.append(num)
                    
                    backtrack()
                    
                    cur_per.pop()
                    visited.remove(num)
            return
    
        backtrack()
        return permutations