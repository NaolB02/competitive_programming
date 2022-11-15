class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 0
        
        while r < len(nums):
            if nums[l] == nums[r]:
                count += 1
                
                if count > 2:
                    nums.pop(r)
                    count -= 1
                else:
                    r += 1
            
            else:
                l = r
                count = 0
            
            
            
            
          
        