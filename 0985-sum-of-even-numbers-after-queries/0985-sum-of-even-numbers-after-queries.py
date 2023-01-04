class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sumOfEven = 0
        
        for num in nums:
            if num % 2 == 0:
                sumOfEven += num
        
        for query in queries:
            val = query[0]
            index = query[1]
            
            if nums[index] % 2 == 0:
                sumOfEven -= nums[index]
            
            nums[index] += val
            
            if nums[index] % 2 == 0:
                sumOfEven += nums[index]
            
            answer.append(sumOfEven)
        
        return answer