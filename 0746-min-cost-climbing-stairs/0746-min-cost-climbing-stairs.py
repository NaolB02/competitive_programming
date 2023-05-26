class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        memo = {}
        def dp(n):
            if n == 0 or n == 1:
                return cost[n]
            
            if n not in memo:
                memo[n] = cost[n] + min(dp(n - 1), dp(n - 2))
            
            return memo[n]
        return dp(n)