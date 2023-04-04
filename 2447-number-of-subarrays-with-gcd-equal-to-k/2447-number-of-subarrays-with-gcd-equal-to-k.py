class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        
        for left in range(len(nums)):
            right = left
            cur_gcd = 0
            
            while right < len(nums):
                cur_gcd = self.gcd(cur_gcd, nums[right])
                
                if cur_gcd < k:
                    break
                
                elif cur_gcd == k:
                    count += 1
                
                right += 1
                
        
        return count
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)