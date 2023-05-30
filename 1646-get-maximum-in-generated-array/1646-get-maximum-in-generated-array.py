class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {0 : 0}
        
        if n > 0:
            memo[1] = 1
            
        def dp(n):
            if n == 0 or n == 1 or n == -1:
                return n
            
            if n not in memo:
                memo[n] = dp(n // 2) if n % 2 == 0 else (dp(n // 2) + dp(n // 2 + 1))
            
            return memo[n]
        
        for i in range(n + 1):
            dp(i)
        return max(memo.values())