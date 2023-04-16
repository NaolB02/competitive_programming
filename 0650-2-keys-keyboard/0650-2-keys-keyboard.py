class Solution:
    def minSteps(self, n: int) -> int:
        factorization = []
        d = 2
        tot = n

        while d * d <= n:
            count = 0

            while n % d == 0:
                n //= d
                count += 1
            
            if count:
                factorization.append([d, count])
            d += 1
        
        if n > 1:
            factorization.append([n, 1])

        min_op = 0
        for prime, count in factorization:
            min_op += prime * count
        
        return min_op