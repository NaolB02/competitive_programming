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


    def connected(self, x, y, z):
        return self.representative(x) == self.representative(y) or self.representative(x) == self.representative(z)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        union = UnionFind(n)
        
        for node1, node2, weight in roads:
            union.union(node1 - 1, node2 - 1)
        
        min_weight = math.inf
        for node1, node2, weight in roads:
            if union.connected(node1 - 1, 0, n - 1) or union.connected(node2 - 1, 0, n - 1):
                min_weight = min(min_weight, weight)
        
        return min_weight