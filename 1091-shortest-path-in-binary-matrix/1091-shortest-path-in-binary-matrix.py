class Solution:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    def inbound(self, n, x, y):
        return 0 <= x < n and 0 <= y < n
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        src, dest = (0, 0), (len(grid) - 1, len(grid) - 1)
        path = {src : None}      
        queue = deque([src])
        goal = None
        
        while queue:
            parent = queue.popleft()
            px, py = parent
            
            if parent == dest:
                goal = parent
                break
            
            for x, y in self.directions:
                nx, ny = px + x, py + y
                
                if (nx, ny) not in path and self.inbound(len(grid), nx, ny) and grid[nx][ny] == 0:
                    queue.append((nx, ny))
                    path[(nx, ny)] = parent
        
        if goal:
            current = goal
            count = 0
            
            while current:
                count += 1
                current = path[current]
            
            return count
    
        else:
            return -1
                
            