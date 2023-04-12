class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        original_col = image[sr][sc]

        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row, col):  
            nonlocal color
            nonlocal original_col
            
            visited[row][col] = True
            image[row][col] = color
            
            for rch, cch in directions:
                n_row = row + rch
                n_col = col + cch

                if inbound(n_row, n_col) and not visited[n_row][n_col] and image[n_row][n_col] == original_col:
                    dfs(n_row, n_col)
                             
        dfs(sr, sc)
        return image