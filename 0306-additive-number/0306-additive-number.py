class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        nums = []
        
        def check_add(arr):
            return len(arr) > 2 and arr[-3] + arr[-2] == arr[-1]
        
        def backtrack(i):
            if i == len(num) and check_add(nums):
                return True
            
            if len(nums) > 2 and nums[-3] + nums[-2] != nums[-1]:
                return
            
            for j in range(i + 1, len(num) + 1):
                cur = num[i:j]
                
                if len(cur) != len(str(int(cur))):
                    continue
                
                nums.append(int(cur))
                res = backtrack(j)
                
                if res:
                    return True
                
                nums.pop()
        
            return False
        
        return backtrack(0)
                
                