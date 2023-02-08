class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end =  len(numbers) - 1
        
        while start < end:
            curSum = numbers[start] + numbers[end]
            
            if curSum < target:
                start += 1
            
            elif curSum > target:
                end -= 1
            
            else:
                return [start + 1, end + 1]