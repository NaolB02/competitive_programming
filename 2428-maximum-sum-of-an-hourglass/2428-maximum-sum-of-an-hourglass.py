class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxSum = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i in range(1, n - 1) and j in range(1, m - 1):
                    upper = grid[i - 1][j] + grid[i - 1][j - 1] + grid[i - 1][j + 1]
                    lower = grid[i + 1][j] + grid[i + 1][j - 1] + grid[i + 1][j + 1]
                    curSum = grid[i][j] + upper + lower
                    maxSum = max(maxSum, curSum)
            
        return maxSum
