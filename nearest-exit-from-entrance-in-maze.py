class Solution:
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    def inbound(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
    
    def isExit(self, row, col, m, n):
        return row == 0 or row == m - 1 or col == 0 or col == n - 1
        
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        entrance = (entrance[0], entrance[1])
        frontier = deque([entrance])
        path = {entrance: None}
        exit = None
        
        while frontier:
            row, col = frontier.popleft()
            
            if (row, col) != entrance and self.isExit(row, col, m, n):
                exit = (row, col)
                break
            
            for dx, dy in self.directions:
                nrow, ncol = row + dx, col + dy
                
                if self.inbound(nrow, ncol, m, n) and maze[nrow][ncol] == '.' and (nrow, ncol) not in path:
                    frontier.append((nrow, ncol))
                    path[(nrow, ncol)] = (row, col)
        
        steps = -1
        while exit:
            exit = path[exit]
            steps += 1
        
        return steps