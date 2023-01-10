class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.temp = 0

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.temp += 1
        
        else:
            self.temp = 0
        
        if self.temp < self.k:
            return False
        
        return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)