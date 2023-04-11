class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False for i in range(len(grid2[0]))] for j in range(len(grid2))]

        def inbound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])

        def dfs(row, col, flag): 
            if not grid1[row][col]:
                flag = False
                
            visited[row][col] = True
            
            for rch, cch in directions:
                n_row = row + rch
                n_col = col + cch

                if inbound(n_row, n_col) and not visited[n_row][n_col] and grid2[n_row][n_col]:
                    flag = dfs(n_row, n_col, flag)
                     
            if flag == None:
                return True
            
            return flag   
        
        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] and not visited[r][c]:
                    cur = dfs(r, c, None)           
                    if cur:
                        count += 1
                    
        return count
        
        