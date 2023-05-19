class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def representative(self, x):
        if self.root[x] != x:
            self.root[x] = self.representative(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x = self.representative(x)
        root_y = self.representative(y)

        if root_x != root_y: 
            if self.size[root_y] > self.size[root_x]:
                root_x, root_y = root_y, root_x

            self.root[root_y] = root_x
            self.size[root_x] += self.size[root_y]


    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
    
class Solution:
    neighbours = {1: [(0, -1), (0, 1)], 2: [(1, 0), (-1, 0)], 3: [(0, -1), (1, 0)], 4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]}
    
    def convert_to_unique_id(self, r, c, n):
        return r * n + c
    
    def isConnected(self, st_coord, neigh_coord, neighbour):
        neighs = []
        x, y = neigh_coord
        
        for dx, dy in self.neighbours[neighbour]:
            neighs.append((x + dx, y + dy))
        
        if st_coord in neighs:
            return True
        
        return False
    
    def inbound(self, m, n, x, y):
        return 0 <= x < m and 0 <= y < n
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        union = UnionFind(m * n)
        
        for r in range(m):
            for c in range(n):
                street = grid[r][c]
                
                for dx, dy in self.neighbours[street]:
                    new_x, new_y = r + dx, c + dy
                    
                    if self.inbound(m, n, new_x, new_y) and self.isConnected((r, c), (new_x, new_y), grid[new_x][new_y]):
                        u1, u2 = self.convert_to_unique_id(r, c, n), self.convert_to_unique_id(new_x, new_y, n)
                        union.union(u1, u2)
        
        return union.connected(0, m * n - 1)
                        
                
                
                
                
                
                
        
        