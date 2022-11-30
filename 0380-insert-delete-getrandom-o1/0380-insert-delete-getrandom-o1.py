class RandomizedSet:

    def __init__(self):
        self.hashmp = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmp:
            return False
        self.hashmp[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmp:
            return False
            
        curInd = self.hashmp[val]

        self.hashmp[self.arr[-1]] = curInd
        self.arr[curInd], self.arr[-1] = self.arr[-1], self.arr[curInd]

        self.arr.pop()       
        del self.hashmp[val]
        return True

    def getRandom(self) -> int:
        rn = randint(0, len(self.arr) - 1)
        return self.arr[rn]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()