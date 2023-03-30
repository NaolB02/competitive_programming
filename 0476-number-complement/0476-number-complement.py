class Solution:
    def findComplement(self, num: int) -> int:
        bin_rep = bin(num)
        complement = []
        
        for bit in bin_rep[2:]:
            if bit == '0':
                complement.append('1')
                continue
                
            complement.append('0')
        
        return int(''.join(complement), 2)