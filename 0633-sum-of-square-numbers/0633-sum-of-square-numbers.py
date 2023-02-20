class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(c ** (1 / 2))
        
        while start <= end:
            sumOfSq = pow(start, 2) + pow(end, 2)
            
            if sumOfSq == c:
                return True
            
            elif sumOfSq < c:
                start += 1
                
            else:
                end -= 1
            
        return False