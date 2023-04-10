class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            cur = 1
            
            visited[row][col] = True
            
            for rch, cch in directions:
                n_row = row + rch
                n_col = col + cch

                if inbound(n_row, n_col) and not visited[n_row][n_col] and grid[n_row][n_col]:
                    cur += dfs(n_row, n_col)
                     
            
            return cur
        
        max_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and not visited[r][c]:
                    cur = dfs(r, c)
                    max_count = max(max_count, cur)
                    
        return max_count