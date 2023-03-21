class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = []
        n = len(nums)
        
        def backtrack(i, cur):            
            if len(cur) > 1 and cur[-1] >= cur[-2]:
                subsequences.append(cur[:])
            
            elif len(cur) > 1 or i == n:
                return
                
            seen = set()
            for j in range(i, n):
                if nums[j] in seen:
                    continue
                cur.append(nums[j])
                backtrack(j + 1, cur)
                cur.pop()
                seen.add(nums[j])
        
        backtrack(0, [])
        return subsequences