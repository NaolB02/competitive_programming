class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        max_sum = 0
        
        if k <= numOnes:
            return k
        
        k -= numOnes
        
        if k <= numZeros:
            return numOnes
        
        k -= numZeros
        
        if k <= numNegOnes:
            return numOnes - k