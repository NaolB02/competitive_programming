class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.calculateGCD(max(nums), min(nums))
    
    def calculateGCD(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return num1
        return self.calculateGCD(num2, num1 % num2)