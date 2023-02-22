class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maximum = windowSum
        
        for end in range(k, len(nums)):
            windowSum -= nums[end - k]
            windowSum += nums[end]
            
            maximum = max(maximum , windowSum)
            
        return maximum/k
            
        