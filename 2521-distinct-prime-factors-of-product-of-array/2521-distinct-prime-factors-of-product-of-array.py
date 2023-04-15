class Solution:
    factorization = set()
    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.factorization = set()
        
        for i in nums:
            if i in self.factorization:
                continue
            
            self.prime_factorizor(i)
        
        return len(self.factorization)
    
    def prime_factorizor(self, n: int) -> list[int]:
        d = 2

        while d * d <= n:
            while n % d == 0:
                self.factorization.add(d)
                n //= d
            d += 1
            
        if n > 1:
            self.factorization.add(n)