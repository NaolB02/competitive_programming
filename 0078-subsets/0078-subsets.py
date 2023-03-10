class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        subset = []
        
        def backtrack(index):
            if index == len(nums):
                if subset:
                    power_set.append(subset[:])
                return
            
            #case - 1
            backtrack(index + 1)
            
            #case - 2
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
        
        backtrack(0)
        return power_set