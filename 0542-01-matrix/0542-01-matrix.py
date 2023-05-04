class Solution:
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    def inbound(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distance_mat = [[0 for i in range(n)] for j in range(m)]
        
        frontier = deque()
        visited = set()
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    frontier.append((r, c, 0))
                    visited.add((r, c))
        
        while frontier:
            r, c, dist = frontier.popleft()
            
            if mat[r][c] == 1:
                distance_mat[r][c] = dist
            
            for dx, dy in self.directions:
                nr, nc = r + dx, c + dy
                
                if not self.inbound(nr, nc, m, n) or (nr, nc) in visited: continue
                visited.add((nr, nc))
                
                frontier.append((nr, nc, dist + 1))
        
        return distance_mat