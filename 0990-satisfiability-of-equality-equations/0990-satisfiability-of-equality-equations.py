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
    def equationsPossible(self, equations: List[str]) -> bool:
        union = UnionFind(26)
        
        for equation in equations:
            letter1, eq1, eq2, letter2 = equation
            letter1, letter2 = ord(letter1) - 97, ord(letter2) - 97
            
            if eq1 == '=':
                union.union(letter1, letter2)
        
        for equation in equations:
            letter1, eq1, eq2, letter2 = equation
            letter1, letter2 = ord(letter1) - 97, ord(letter2) - 97
            
            if eq1 == '=' and not union.connected(letter1, letter2):
                return False
            
            if eq1 == '!' and union.connected(letter1, letter2):
                return False
        
        return True
        