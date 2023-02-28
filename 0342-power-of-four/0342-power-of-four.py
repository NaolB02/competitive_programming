class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 1
        
        while n > num:
            num *= 4
        
        if n == num:
            return True
        
        else:
            return False