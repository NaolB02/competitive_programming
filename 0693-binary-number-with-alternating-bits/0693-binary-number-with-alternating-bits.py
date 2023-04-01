class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        first = 1 & n
        places = int(math.log(n, 2)) + 1
        
        for i in range(places):
            if first != (n & 1):
                return False
            n >>= 1
            first ^= 1
        
        return True