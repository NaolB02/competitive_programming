class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin(x ^ y)
        count = 0
        
        for bit in xor:
            if bit == '1':
                count += 1
        
        return count