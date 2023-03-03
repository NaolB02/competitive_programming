class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        
        while low < high:
            mid = low + (high - low + 1) // 2
            
            if mid * mid > x:
                high = mid - 1
            
            else:
                low = mid
        
        return low