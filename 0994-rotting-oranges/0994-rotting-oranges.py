class Solution:
    def getNeighbours(self, grid, row, col):
        neighbours = []
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        
        for x, y in directions:
            if 0 <= row + x < len(grid) and 0 <= col + y < len(grid[0]):
                neighbours.append((row + x, col + y))
        
        return neighbours
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        onecount = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                
                elif grid[row][col] == 1:
                    onecount += 1
        
        minutes = 0
        while queue:
            n = len(queue)
            minutes += 1
            
            for _ in range(n):
                row, col = queue.popleft()
                neighbours = self.getNeighbours(grid, row, col)
                
                for nr, nc in neighbours:
                    if grid[nr][nc] == 1:
                        onecount -= 1
                        queue.append((nr, nc))
                        grid[nr][nc] += 1
        
        if onecount == 0 and minutes > 0:
            return minutes - 1
        
        elif onecount == 0:
            return 0
        
        return -1