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
        
        else:
            return 'repeated'


    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        max1, max2 = max(edges, key=lambda x: x[0])[0], max(edges, key=lambda x: x[1])[1]
        unionfind = UnionFind(max(max1, max2))
        
        for node1, node2 in edges:
            a = unionfind.union(node1 - 1, node2 - 1)
            
            if a == 'repeated':
                return [node1, node2]
            
        return []